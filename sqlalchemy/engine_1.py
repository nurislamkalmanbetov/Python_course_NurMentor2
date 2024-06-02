from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Создайте соединение с базой данных
engine = create_engine('mysql+pymysql://root:qwerty123@localhost/test2')

# Создайте таблицы, если они еще не существуют
Base.metadata.create_all(engine)

# Создайте сессию
Session = sessionmaker(bind=engine)
session = Session()


def get_session():
    engine = create_engine('mysql+pymysql://root:qwerty123@localhost/test2')
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
