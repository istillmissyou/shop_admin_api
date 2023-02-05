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
    '''URL к БД'''
    user = os.getenv('POSTGRES_USER', 'postgres')
    password = os.getenv('POSTGRES_PASSWORD', '')
    server = os.getenv('POSTGRES_SERVER', 'db')
    db = os.getenv('POSTGRES_DB', 'app')
    port = os.getenv('POSTGRES_PORT')
    return f'postgresql://{user}:{password}@{server}:{port}/{db}'


def write_notification(name: str):
    '''Фоновая задача с записью в файл о новом созданном товаре'''
    with open("log.txt", mode="w") as log_file:
        content = f'Добавлен новый товар {name}'
        log_file.write(content)
