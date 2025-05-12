-- SQLite
SELECT * from fornecedores;

SELECT * from produtos;

SELECT fornecedores.nome, SUM(produtos.preco) AS total_preco
FROM produtos
JOIN fornecedores ON produtos.fornecedor_id = fornecedores.id
GROUP BY fornecedores.nome;