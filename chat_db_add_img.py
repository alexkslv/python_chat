from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chat_db import ImageDB

def db_add_image(name, imgData):
    engine = create_engine('sqlite:///chat.db')
    DBsession = sessionmaker(bind=engine)
    newImage = ImageDB(name=name, img=imgData)
    session = DBsession()
    session.add(newImage)
    session.commit()
    session.close()


