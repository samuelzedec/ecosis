from pydantic import BaseModel

class Doacao(BaseModel):
    nome_usuario: str
    valor: float