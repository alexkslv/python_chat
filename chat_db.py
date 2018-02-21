from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class ImageDB(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    img = Column(BLOB)

engine = create_engine('sqlite:///chat.db')

Base.metadata.create_all(engine)
