from fastapi import FastAPI
from app.models.campanha import Campanha
from app.models.voluntario import Voluntario
from app.models.doacao import Doacao
from app.libs.db import DataBase

app = FastAPI()
db = DataBase()

@app.get("/all_campanhas")
def all_campanhas():
    campanhas = db.get_all_campanhas()
    return campanhas

@app.post("/criar-campanha")
async def criar_campanha(campanha: Campanha):
    try:
        data = dict()
        data = campanha.dict()
        db.salvar_campanha(data)
        return "Campanha criada com Sucesso!"
    except Exception as e:
        return {"message": f"{e}"}

@app.get("/campanha/{campanha_id}")
async def get_campanha(campanha_id: int):
    try:
        response = db.get_campanha(campanha_id)
        return response
    except Exception as e:
        return {"message": f"{e}"}

@app.post("/campanha/{campanha_id}/adicionar-voluntario")
async def adicionar_voluntario(campanha_id: int, voluntario: Voluntario):
    try:
        voluntario_data = voluntario.dict()
        db.salvar_voluntario(campanha_id, voluntario_data)
        return "Voluntário Adicionado a Campanha!"

    except Exception as e:
        return {"message": f"{e}"}

@app.post("/campanha/{campanha_id}/adicionar-doacao")
async def adicionar_doacao(campanha_id: int, doacao: Doacao):
    try:
        doacao_data = doacao.dict()
        db.salvar_doacao(campanha_id, doacao_data)
        return "Doação Adicionado a Campanha!"

    except Exception as e:
        return {"message": f"{e}"}
        