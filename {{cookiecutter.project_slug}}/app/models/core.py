from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    updated_at = Column(DateTime, default=datetime.now)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), index=True, unique=True)
    email = Column(String(255), index=True, unique=True)
    password_hash = Column(db.String(128))

    def __repr__(self):
        return f'<User(username={self.username})>'
