from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select, text

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


engine = create_engine("sqlite:///database.db", echo=True)

# INSERT

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()

# SELECT 1

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     hero = session.exec(statement).first()
#     print(hero)


# SELECT 2

# with Session(engine) as session:
#     statement = text("SELECT * FROM hero WHERE id IN (4,5,6);")    
#     exec_query = session.execute(statement)
#     heroes = exec_query.fetchall()

#     for hero in heroes:
#         print(hero)

# DELETE

# with Session(engine) as session:
#     statement = text("DELETE FROM hero WHERE id IN (4, 5, 6);")
#     session.exec(statement)
#     session.commit()