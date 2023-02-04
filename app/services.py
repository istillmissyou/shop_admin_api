from dotenv import load_dotenv
import os

import database

load_dotenv()


def add_tables():
    '''Добавление таблиц в БД'''
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_url():
    user = os.getenv('POSTGRES_USER', 'postgres')
    password = os.getenv('POSTGRES_PASSWORD', '')
    server = os.getenv('POSTGRES_SERVER', 'db')
    db = os.getenv('POSTGRES_DB', 'app')
    port = os.getenv('POSTGRES_PORT')
    return f'postgresql://{user}:{password}@{server}:{port}/{db}'
