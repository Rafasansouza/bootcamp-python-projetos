# Conectando ao SQLite

from sqlalchemy import create_engine

engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexao com SQLite estabelecida.")

# definindo os modelos e criando tabelas correspondentes no banco de dados

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

Base.metadata.create_all(engine)

#Criando sessao e iniciando dados
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("Usuário inserido com sucesso.")

# consultando dados

usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")

# Exemplo Sem Usar with

from sqlalchemy.orm import sessionmaker
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)
session = Session()

try:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

# Exemplo Usando with

from sqlalchemy.orm import sessionmaker, Session
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)