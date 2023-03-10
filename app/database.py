from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

import services

DATABASE_URL = services.get_url()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    pass
