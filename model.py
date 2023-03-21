import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sql.Column(sql.Integer, primary_key = True)
    name = sql.Column(sql.String(length=50), unique=True, nullable=False)

    def __str__(self):
        return f"Имя издателя - {self.name}"

class Book(Base):
    __tablename__ = 'book'

    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String(length=75), nullable=False)
    id_publisher = sql.Column(sql.Integer, sql.ForeignKey('publisher.id'), nullable=False)

    def __str__(self):
        return f"Название книги - {self.title}"

    publisher = relationship(Publisher, backref='books')

class Shop(Base):
    __tablename__ = 'shop'

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(length=30), unique=True, nullable=False)

    def __str__(self):
        return f"Название магазина - {self.name}"

class Stock(Base):
    __tablename__ = 'stock'

    id = sql.Column(sql.Integer, primary_key=True)
    count = sql.Column(sql.Integer)
    id_book = sql.Column(sql.Integer, sql.ForeignKey('book.id'), nullable=False)
    id_shop = sql.Column(sql.Integer, sql.ForeignKey('shop.id'), nullable=False)

    def __str__(self):
        return f"Количество книг на складе - {self.count}"

    shop = relationship(Shop, backref='stocks')
    book = relationship(Book, backref='stocks')

class Sale(Base):
    __tablename__ = 'sale'

    id = sql.Column(sql.Integer, primary_key=True)
    price = sql.Column(sql.Float, nullable=False)
    count = sql.Column(sql.Integer, nullable=False)
    date_sale = sql.Column(sql.Date, nullable=False)
    id_stock = sql.Column(sql.Integer, sql.ForeignKey('stock.id'), nullable=False)

    def __str__(self):
        return f"| Цена продажи - {self.price} | Дата продажи - {self.date_sale} |"

    stock = relationship(Stock, backref='sales')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)