from database import Base, SessionLocal, engine


def add_tables():
    '''Добавление таблиц в БД'''
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
