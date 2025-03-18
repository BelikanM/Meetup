from flask import render_template
from flask_app import app
from flask_app.models import Utilisateur

@app.route('/')
def index():
    utilisateurs = Utilisateur.query.all()
    return render_template('index.html', utilisateurs=utilisateurs)
