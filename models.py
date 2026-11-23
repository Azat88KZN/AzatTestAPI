from database import Base
from sqlalchemy import Column, Float, Integer, String


class ItemDB(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  price = Column(Float)
