import requests


# requests.get # select

# requests.post # create

# requests.put # update

# requests.delete # delete

from pydantic import BaseModel

class PokemonSchame(BaseModel): # Contrato de dados, schema de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True

def Pegar_info_pokemon(id: int) -> PokemonSchame:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_types = data['types']
    types_list = []
    for types in data_types:
        types_list.append(types['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchame(name=data['name'], type=types)

if __name__ == "__main__":
    print(Pegar_info_pokemon(10))
    print(Pegar_info_pokemon(6))
    print(Pegar_info_pokemon(13))