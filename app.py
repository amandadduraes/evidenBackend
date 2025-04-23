from flask import Flask, request, jsonify
from datetime import datetime
import re
import unicodedata 

app = Flask(__name__)
CORS(app)


# Lista em memória para armazenar os livros, já que não utilizo banco de dados
bookmarks = []

# Função para normalizar strings (remove acentos, deixando tudo minúsculo)
def normalize(text):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower()

@app.route('/bookmarks', methods=['GET'])
def get_bookmarks():
    sorted_bookmarks = sorted(bookmarks, key=lambda x: x['remember_date'])
    return jsonify(sorted_bookmarks)

@app.route('/bookmarks', methods=['POST'])
def add_bookmark():
    data = request.get_json()

    if not all(k in data for k in ('title', 'url', 'remember_date')):
        return jsonify({'error': 'Missing fields'}), 400

    try:
        datetime.strptime(data['remember_date'], '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format (use YYYY-MM-DD)'}), 400

    if not data['url'].startswith(('http://', 'https://')):
        return jsonify({'error': 'URL must start with http:// or https://'}), 400

    bookmarks.append(data)
    return jsonify({'message': 'Bookmark added successfully'}), 201

@app.route('/bookmarks/<string:title>', methods=['DELETE'])
def delete_bookmark(title):
    global bookmarks
    normalized_title = normalize(title)
    before = len(bookmarks)

    bookmarks = [
        b for b in bookmarks
        if normalize(b['title']) != normalized_title
    ]

    after = len(bookmarks)

    if before == after:
        return jsonify({'error': 'Bookmark not found'}), 404

    return jsonify({'message': 'Bookmark deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
