from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps
import json
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'

# Verificar se Flask está instalado, senão instala automaticamente
try:
    import flask
except ImportError:
    subprocess.check_call(['pip3', 'install', 'flask'])

# Caminho para o ficheiro de utilizadores
USER_FILE = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

# Decorador para proteger páginas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return render_template('index.html', user=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuarios = carregar_usuarios()
        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        return render_template('login.html', erro='Credenciais inválidas')
    return render_template('login.html', erro=None)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6500, debug=True)
