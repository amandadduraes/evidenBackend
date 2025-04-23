# 🧠 Bookmark Manager — Backend (Flask)

API REST simples para cadastrar, listar e deletar bookmarks (título, URL e data para lembrar).  
Este backend serve como base para o projeto frontend em React.

---

## 🚀 Tecnologias usadas

- **Python 3**
- **Flask**
- **Flask-CORS** (para integração com o frontend)
- **JSON** como estrutura de dados
- **In-memory** (sem banco de dados por simplicidade)

---

## 📦 Como rodar

### 1. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2.Instale as dependências:
```bash
pip install flask flask-cors
```
### 3.Execute a aplicação:
```bash
python app.py
```
A API estará disponível em: http://localhost:5000

## 📚 Endpoints disponíveis

| Método | Rota                | Descrição                      |
|--------|---------------------|--------------------------------|
| GET    | /bookmarks          | Lista todos os bookmarks       |
| POST   | /bookmarks          | Adiciona um novo bookmark      |
| DELETE | /bookmarks/<title>  | Remove bookmark pelo título    |



## 📄 Exemplo de requisição POST
```bash
POST /bookmarks
Content-Type: application/json
{
  "title": "O mundo de Sophia",
  "url": "https://mundodesophia.com",
  "remember_date": "2025-04-22"
}
```

## ✅ Validações implementadas
Campos obrigatórios (title, url, remember_date)

URL deve começar com http:// ou https://

Data deve estar no formato YYYY-MM-DD


