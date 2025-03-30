import os
import json

# Estrutura de pastas
pastas = [
    "templates",
    "static/css"
]

# Conteúdo dos ficheiros
usuarios_json = {
    "andre": "senha123",
    "socio": "senha456"
}

login_html = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/login.css') }}">
</head>
<body>
    <div class="login-box">
        <h2>Login</h2>
        {% if erro %}
            <p class="erro">{{ erro }}</p>
        {% endif %}
        <form method="POST">
            <input type="text" name="username" placeholder="Utilizador" required>
            <input type="password" name="password" placeholder="Palavra-passe" required>
            <button type="submit">Entrar</button>
        </form>
    </div>
</body>
</html>
"""

index_html = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Página Principal</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
</head>
<body>
    <div class="container">
        <h1>Bem-vindo, {{ user }}!</h1>
        <p>Este é o painel principal.</p>
        <a href="{{ url_for('logout') }}">Sair</a>
    </div>
</body>
</html>
"""

login_css = """body {
    background: #f2f2f2;
    font-family: Arial, sans-serif;
}
.login-box {
    width: 300px;
    margin: 80px auto;
    padding: 30px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
.login-box h2 {
    text-align: center;
}
.login-box input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
}
.login-box button {
    width: 100%;
    padding: 10px;
    background: #333;
    color: white;
    border: none;
    cursor: pointer;
}
.erro {
    color: red;
    text-align: center;
}
"""

index_css = """body {
    background: #ffffff;
    font-family: Arial, sans-serif;
    text-align: center;
    padding-top: 60px;
}
.container {
    max-width: 500px;
    margin: auto;
}
.container a {
    text-decoration: none;
    color: #fff;
    background: #007bff;
    padding: 10px 20px;
    border-radius: 5px;
}
"""

# Criar pastas
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)

# Criar ficheiros
with open("usuarios.json", "w") as f:
    json.dump(usuarios_json, f, indent=4)

with open("templates/login.html", "w", encoding="utf-8") as f:
    f.write(login_html)

with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("static/css/login.css", "w", encoding="utf-8") as f:
    f.write(login_css)

with open("static/css/index.css", "w", encoding="utf-8") as f:
    f.write(index_css)

print("✅ Estrutura criada com sucesso!")
