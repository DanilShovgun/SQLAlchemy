from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import Publisher, Book, Stock, Sale, Shop

engine = create_engine('postgresql://user:password@host/dbname')
Session = sessionmaker(bind=engine)
session = Session()

publisher_name = input("Введите имя издателя: ")

publisher = session.query(Publisher).filter_by(name=publisher_name).first()

if publisher:
    sales = session.query(Sale, Book, Shop).join(Stock).join(Book).join(Publisher).join(Shop).filter(Publisher.name == publisher_name).all()
    for sale, book, shop in sales:
        print(f"{book.title} | {shop.name} | {sale.price} | {sale.date_sale.strftime('%d-%m-%Y')}")
else:
    print("Издатель не найден")
