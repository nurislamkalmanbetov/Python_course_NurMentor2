from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, DECIMAL, Date, DateTime, Text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Players(Base):
    __tablename__ = 'players'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nickname = mapped_column(String(50), unique=True)
    rank = mapped_column(String(50))
    level = mapped_column(Integer)
    heroes = relationship("Heroes", back_populates="player")
    teams = relationship("Teams", back_populates="players") # с Teams

class Heroes(Base):
    __tablename__ = 'heroes'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(50), unique=True)
    description = mapped_column(Text)
    level = mapped_column(Integer)
    abilities = mapped_column(Text)
    players_id = mapped_column(Integer, ForeignKey('players.id'))
    player = relationship("Players", back_populates="heroes")

class Teams(Base):
    __tablename__ = 'teams'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(50), unique=True)
    rating = mapped_column(Integer)
    players_id = mapped_column(Integer, ForeignKey('players.id'))
    players = relationship("Players", back_populates="teams")

