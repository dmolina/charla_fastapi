# Create the database
from database import Session, engine
from sqlalchemy import Table, Column, Integer, String

from models import Base, Serie, Category

def main():
    # Creo las tablas
    Base.metadata.create_all(engine)
    comedy = Category(name="Comedy")
    drama = Category(name="Drama")
    session = Session()
    session.add(comedy)
    session.add(drama)
    session.add(Category(name="Musical"))
    session.add(Serie(title="The Big Bang Theory",
                      description="Serie de frikis", category=comedy))
    session.add(Serie(title="Juego de Tronos", description="Todos mueren",
                      category=drama))
    session.commit()


if __name__ == '__main__':
    main()
