import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre_clé_secrète'
    # Remplacez 'utilisateur', 'motdepasse' et 'nom_de_la_base' par vos informations
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://utilisateur:motdepasse@localhost/nom_de_la_base'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
