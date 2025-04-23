produto1: str = "sapato"
produto2: str = "camiseta"
produto3: str = "videogame"

produtos: list = []

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)
produtos.insert(1, "short")
produtos.pop()
produtos.remove(produto1)

print(produtos)
