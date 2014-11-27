from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey, desc, asc, func
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import datetime

# A class that maps to a table, inherits from Base
Base = declarative_base()
spots = [
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]



# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints
class Movie(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float(precision=2))


class Projection(Base):
    __tablename__ = "Projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('Movies.id'))
    type = Column(String)
    date = Column(Date)
    time = Column(Time)


class Reservation(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey('Projections.id'))
    row = Column(Integer)
    col = Column(Integer)


def dbFillin():
    engine = create_engine("sqlite:///cinema.db")
    # will create all tables
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    print("Adding new student to the database via the session object")
    session.add_all([
        Movie(name="The Hunger Games: Catching Fire", rating=7.9),
        Movie(name="Wreck-It Ralph", rating=7.8),
        Movie(name="Her", rating=8.3),
        Projection(movie_id=1, type="3D", date=datetime.date(2014, 4, 1), time=datetime.time(19, 10)),
        Projection(movie_id=1, type="2D", date=datetime.date(2014, 4, 2), time=datetime.time(19, 00)),
        Projection(movie_id=1, type="4DX", date=datetime.date(2014, 4, 3), time=datetime.time(21, 10)),
        Projection(movie_id=3, type="2D", date=datetime.date(2014, 4, 1), time=datetime.time(20, 20)),
        Projection(movie_id=2, type="3D", date=datetime.date(2014, 4, 1), time=datetime.time(22, 00)),
        Projection(movie_id=2, type="2D", date=datetime.date(2014, 4, 1), time=datetime.time(19, 30)),
        Reservation(username="RadoRado", projection_id=1, row=2, col=1),
        Reservation(username="RadoRado", projection_id=1, row=3, col=5),
        Reservation(username="RadoRado", projection_id=1, row=7, col=8),
        Reservation(username="Ivo", projection_id=3, row=1, col=1),
        Reservation(username="Ivo", projection_id=3, row=1, col=2),
        Reservation(username="Mysterious", projection_id=5, row=2, col=3),
        Reservation(username="Mysterious", projection_id=5, row=2, col=4)])

    session.commit()


def show_movies():
    engine = create_engine("sqlite:///cinema.db")
    session = Session(bind=engine)
    all_movies = session.query(Movie).order_by(desc(Movie.rating))
    for movie in all_movies:
        print("[" + str(movie.id) + "]" + movie.name + " " + str(movie.rating))


def show_movie_projections(movie_id1, date=0):
    engine = create_engine("sqlite:///cinema.db")
    session = Session(bind=engine)
    movie_id = int(movie_id1)
    if date == 0:
        movie_projections = session.query(Projection).filter(Projection.movie_id == movie_id).order_by(asc(Projection.date))
        for proj in movie_projections:
            reservations_for_those = session.query(Reservation).filter(proj.id == Reservation.projection_id).count()
            reservations_for_those = 100 - reservations_for_those
            if reservations_for_those == 0:
                reservations_for_those = "No available seats"
            print(str(proj.id) + " " + proj.type + " " + str(proj.date) + " " + str(proj.time) + " Tickets available: " + str(reservations_for_those))
    else:
        print(date)
        movie_projections = session.query(Projection).filter(Projection.movie_id == movie_id, Projection.date == date).order_by(asc(Projection.date))
        for proj in movie_projections:
            reservations_for_those = session.query(Reservation).filter(proj.id == Reservation.projection_id).count()
            reservations_for_those = 100 - reservations_for_those
            if reservations_for_those == 0:
                reservations_for_those = "No available seats"
            print(str(proj.id) + " " + proj.type + " " + str(proj.date) + " " + str(proj.time) + " Tickets available: " + str(reservations_for_those))


def cancel_reservation(name):
    engine = create_engine("sqlite:///cinema.db")
    session = Session(bind=engine)
    session.query(Reservation).filter(Reservation.username == name).delete()
    session.commit()


def show_available_spots(projection_id):
    engine = create_engine("sqlite:///cinema.db")
    session = Session(bind=engine)
    taken_seats = session.query(Reservation).filter(Reservation.projection_id == projection_id)
    for reservation in taken_seats:
        spots[reservation.row-1][reservation.col-1] = "X"
    for row in spots:
        for value in row:
            print(value, end=' ')
        print()


def make_reservation():
    engine = create_engine("sqlite:///cinema.db")
    session = Session(bind=engine)
    username = input("Enter your username: ")
    ticketNum = int(input("Enter number of tickets: "))
    show_movies()
    movie_id_choice = int(input("Choose movie by id: "))
    show_movie_projections(movie_id_choice)
    projection_choice = int(input("Choose projection id: "))
    reservations_for_those = session.query(Reservation).filter(Reservation.projection_id == projection_choice).count()
    available = 100 - reservations_for_those
    if available < ticketNum:
        print("  ==================================================\n||There is no enough tickets for you, try with less||\n  ==================================================")
        return 0
    else:
        show_available_spots(projection_choice)
    for i in range(ticketNum):
        row_choice = int(input("Choose row "))
        col_choice = int(input("Choose col "))
        if row_choice > 0 and row_choice < len(spots) and col_choice > 0 and col_choice < len(spots) and spots[row_choice - 1][col_choice - 1] == ".":
            reseve = Reservation(username=username, projection_id=projection_choice, row=row_choice, col=col_choice)
            session.add(reseve)
            session.commit()
            print("added")
            show_available_spots(projection_choice)
        else:
            print("This seat is already taken. Try another!")
#spots ne se promenq c dr fynkciq
