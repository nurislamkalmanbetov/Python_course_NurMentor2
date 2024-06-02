from engine_1 import engine, Base 
from models import Players, Heroes



def create_tables():
    Base.metadata.create_all(engine,checkfirst=True)
    