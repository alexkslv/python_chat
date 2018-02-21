from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chat_db import ImageDB

def image_from_db(name):
    engine = create_engine('sqlite:///chat.db')
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    imgData = session.query(ImageDB).filter_by(name=name).first()

    if imgData != None:
        data = imgData.img
        session.close()
        return data
    else:
        session.close()
        return -1



