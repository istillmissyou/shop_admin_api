import database
from config import settings


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
    user = settings.postgres_user
    password = settings.postgres_password
    server = settings.postgres_server
    db = settings.postgres_db
    port = settings.postgres_port
    return f'postgresql://{user}:{password}@{server}:{port}/{db}'


def write_notification(name: str):
    '''Фоновая задача с записью в файл о новом созданном товаре'''
    with open("log.txt", mode="w") as log_file:
        content = f'Добавлен новый товар {name}'
        log_file.write(content)
