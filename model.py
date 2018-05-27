from sqlalchemy import Column, Integer, String
from engine import Base
from sqlalchemy.orm import relationship

class User(Base):
    _tablename_ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    addresses = relationship("Address", back_populates="items")

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r, %r>' % (self.name, self.email)