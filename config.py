import os
from dotenv import load_dotenv

load_dotenv()  # Charger les variables d'environnement depuis .env

class Config:
    # Config Appwrite
    APPWRITE_ENDPOINT = os.getenv('APPWRITE_ENDPOINT')
    APPWRITE_PROJECT_ID = os.getenv('APPWRITE_PROJECT_ID')
    APPWRITE_API_KEY = os.getenv('APPWRITE_API_KEY')

    # Config MySQL
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    
    # Secret Key
    SECRET_KEY = os.getenv('SECRET_KEY')  # Charger la clé secrète depuis .env
