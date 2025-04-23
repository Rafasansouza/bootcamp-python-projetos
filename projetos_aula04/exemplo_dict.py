import json

produto1: dict = {
    "nome": "Sapato",
    "quantidade": 39,
    "preco": 110.38,
    "disponibilidade": True
}

produto2: dict = {
    "nome": "Televisao",
    "quantidade": 10,
    "preco": 3110.38,
    "disponibilidade": False
}


carrinho: list = []

carrinho.append(produto1)
carrinho.append(produto2)

carrinho_json = json.dumps(carrinho) #json.dumps() transforma um dicionario em um json (dicionario do javascript)

print(carrinho_json)

#Crie um dicionario para armazenar informações de um livro,
#incluido título, autor e ano de publicação. imprima cada informação.

from typing import Dict, Any

livro1: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "George R. R. Martin",
    "Ano": 1996
}

livro2: Dict[str, Any] = {
    "Titulo": "Harry Potter e a Pedra Filosofal",
    "Autor": "J.K. Rowling",
    "Ano": 1997
}

lista_de_livros: list = []

lista_de_livros.append(livro1)
lista_de_livros.append(livro2)

print(lista_de_livros)

lista_de_livros_usando_Dict: Dict = {
    "livro1": {
        "Titulo": "Game of Thrones",
        "Autor": "George R. R. Martin",
        "Ano": 1996
    },
    "livro2": {
        "Titulo": "Harry Potter e a Pedra Filosofal",
        "Autor": "J.K. Rowling",
        "Ano": 1997
    }
}

print(lista_de_livros_usando_Dict)

print(lista_de_livros_usando_Dict["livro1"])

print(lista_de_livros_usando_Dict["livro1"]["Titulo"])

print(lista_de_livros_usando_Dict["livro1"]["Autor"])

print(lista_de_livros_usando_Dict["livro1"]["Ano"])