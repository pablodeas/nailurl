import os
import secrets
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = secrets.token_hex(16)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

USERNAME = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOSTNAME = os.getenv('POSTGRES_HOST')
DATABASE = os.getenv('POSTGRES_DB')

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_POOL_RECYCLE'] = 229
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def random_string(length=5):
    """Generate a random string of fixed length."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(secrets.choice(characters) for _ in range(length))

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.short_url}'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/encurtar', methods=['GET', 'POST'])
def encurtar():
    if request.method == 'POST':
        url = request.form['url']
        # Adiciona 'http://' se o esquema não estiver presente
        if not url.startswith(('http://', 'https://')):
            url = f'http://{url}'
        
        short_url = random_string(5)  # Apenas o identificador curto
        new_url = Url(url=url, short_url=short_url)  # Salva apenas o identificador curto
        db.session.add(new_url)
        db.session.commit()
        full_short_url = f'{short_url}'
        return render_template('index.html', short_url=full_short_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    url_entry = Url.query.filter_by(short_url=short_url).first()
    if url_entry:
        return redirect(url_entry.url)  # Redireciona para a URL original
    else:
        flash('URL não encontrada!', 'error')
        return render_template('index.html')  # Retorna à página inicial com uma mensagem de erro

if __name__ == "__main__":
    app.run(debug=True)