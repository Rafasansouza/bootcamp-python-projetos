from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados, schema de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True