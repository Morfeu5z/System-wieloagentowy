from . import _Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationships


class Memory(_Base):
    '''
    * Model dla pamięci agentów
    '''
    __tablename__ = 'memory'
    id = Column(Integer, primary_key=True)
    deviceID = Column(Integer)
    type = Column(String(50))
    sold = Column(Integer)

    def __init__(self, deviceID, type, sold):
        self.deviceID = deviceID
        self.type = type
        self.sold = sold
