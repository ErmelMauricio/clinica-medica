# Conexão com o Mongo.

import os
from bson import ObjectId
from pymongo import MongoClient

cliente = MongoClient(os.environ.get("MONGO_URL", "mongodb://localhost:27017"), serverSelectionTimeoutMS=3000)

banco = cliente["agenda_medica_demo"]


def buscar_por_id(colecao, id_):
    if not id_:
        return None
    return colecao.find_one({"_id": ObjectId(id_)})

