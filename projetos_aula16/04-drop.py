from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text


# Supondo que o banco de dados seja SQLite e esteja no arquivo `database.db`
engine = create_engine("sqlite:///database.db")

# Criação da sessão
with Session(engine) as session:
    statement = text("DROP TABLE hero;")
    results = session.execute(statement)
    session.exec(statement)
    session.commit()