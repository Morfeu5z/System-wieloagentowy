from . import _Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationships

class Items(_Base):
    '''
    * Model dla tabeli items
    '''
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))
    weight = Column(Float)
    cpu = Column(Integer)
    gpu = Column(Integer)
    battery = Column(Integer)
    dec = Column(Integer)
    price = Column(Float)
    procesor = Column(String(50))
    grafika = Column(String(50))
    device = Column(String(50))
    sold = Column(Integer)

    def __init__(self, name, type, weight, cpu, gpu, battery, dec, price, procesor, grafika):
        self.name = name
        self.type = type
        self.weight = weight
        self.cpu = cpu
        self.gpu = gpu
        self.battery = battery
        self.dec = dec
        self.price = price
        self.procesor = procesor
        self.grafika = grafika
#
# class Sold(_Base):
#     '''
#     * Model dla tabeli items
#     '''
#     __sold__ = 'sold'
#     id = Column(Integer, primary_key=True)
#     type = Column(String(50))
#     device = Column(Integer)
#     sold = Column(Integer)
#
#     def __init__(self, type, device, sold):
#         self.type = type
#         self.device = device
#         self.sold = sold
