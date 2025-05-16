from pydantic import BaseModel

class Campanha(BaseModel):
    nome_campanha: str
    meta: str
    data_final: str
    tipo_ajuda: str