from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class Website(Base):
    __tablename__ = "Website"
    id = Column(Integer, primary_key=True)
    URL = Column(String)
    title = Column(String)
    description = Column(String)
    HTML_version = Column(String)


def createDB():
    engine = create_engine("sqlite:///info.db")
    # will create all tables
    Base.metadata.create_all(engine)


def addPage(URL, title, description, HTML_version):
    engine = create_engine("sqlite:///info.db")
    session = Session(bind=engine)
    new = Website(URL=URL, title=title, description=description, HTML_version=HTML_version)
    session.add(new)
    session.commit()



#bez# v url
