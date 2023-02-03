from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        index=True,
        unique=True,
    )


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        index=True,
        unique=True,
    )
    price: Mapped[int] = mapped_column(index=True)
    count: Mapped[int] = mapped_column(index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship()
