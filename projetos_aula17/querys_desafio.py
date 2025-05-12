from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from desafio import Fornecedor, Produto, engine
# Supondo que engine já foi definido anteriormente e os modelos Produto e Fornecedor foram definidos conforme o exemplo anterior.

Session = sessionmaker(bind=engine)
session = Session()

qtde_fornecedores = session.query(
    func.count(Fornecedor.id).label('total_fornecedores')
).scalar()

print(f'Ha {qtde_fornecedores} registros na table Fornecedores')

qtde_produtos = session.query(
    func.count(Produto.id).label('total_produtos')
).scalar()

print(f'Ha {qtde_produtos} registros na table produtos')

resul_join = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resul_join:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")