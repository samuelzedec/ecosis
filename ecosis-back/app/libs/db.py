from app.config.settings import ENV, DATABASE_HOST, DATABASE_PORT
from pymongo import MongoClient, ReturnDocument


class DataBase(object):

    if ENV == "prod":
        db: MongoClient = MongoClient(
            f"mongodb://{DATABASE_HOST}:{DATABASE_PORT}/"
            f"?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.8")["DoaAM"] # type: ignore

    def salvar_campanha(self, data: dict) -> dict:
        try:
            data["_id"] = self.get_next_id("campanha_id")
            data["voluntarios"] = []
            data["doacoes"] = []
            self.db.campanha.insert_one(data)
        except Exception as e:
            return {"message": f"{e}"}

    def get_campanha(self, campanha_id: int):
        try:
            result = self.db.campanha.find_one({"_id": campanha_id})
            return result
        except Exception as e:
            return {"message": f"{e}"}
        
    def get_all_campanhas(self):
        try:
            campanhas = self.db.campanha.find()
            result = [campanha for campanha in campanhas]
            return result
        except Exception as e:
            return {"message": f"{e}"}

    def get_next_id(self, sequence_name):
        doc = self.db.counters.find_one_and_update(
            {"_id": sequence_name},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return doc["seq"]
    
    def salvar_voluntario(self, campanha_id: int, voluntario_infos: dict):
        try:
            self.db.campanha.update_one(
            {"_id": campanha_id},
            {"$push": {"voluntarios": voluntario_infos}})
        except Exception as e:
            return {"message": f"{e}"}
    
    def salvar_doacao(self, campanha_id: int, doacao_infos: dict):
        try:
            self.db.campanha.update_one(
            {"_id": campanha_id},
            {"$push": {"doacoes": doacao_infos}})
        except Exception as e:
            return {"message": f"{e}"}