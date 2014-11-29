from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, asc, update
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    points = Column(Integer)


def createDb():
    engine = create_engine("sqlite:///math.db")
    # will create all tables
    Base.metadata.create_all(engine)


def highscores():
    print("This is the current top10:")
    engine = create_engine("sqlite:///math.db")
    session = Session(bind=engine)
    top = session.query(User).order_by(asc(User.points))
    for player in top:
        print(player.name + " - " + str(player.points))


def writeInDb(username, points):
    engine = create_engine("sqlite:///math.db")
    session = Session(bind=engine)
    isThere = session.query(User).filter(User.name == username).first()
    try:
        if isThere.name:
            oldPoints = session.query(User.points).filter(User.name == username).first()
            if oldPoints[0] > points:
                print("You have already played this game and your previos \nresult is better than now so I wont save this points!")
            else:
                session.query(User).filter(User.name == username).update({'points': points})
                session.commit()

    except Exception:
        add = User(name=username, points=points)
        session.add(add)
        session.commit()
        print("added")
