from sqlalchemy import select
from fastapi import APIRouter
from models.db import mediciones_presion
from models.db import usuarios
from config.db import conn
from API.schemas.base_models import Data, DataPressure, User

data_user = APIRouter()

@data_user.get("/data_user/{id}", response_model=list[DataPressure], tags=["data"])
def read_data_users(id: int):
    # Usar select() correctamente
    query = select(mediciones_presion.c.presion_sistolica, mediciones_presion.c.presion_diastolica).where(mediciones_presion.c.id_usuario == id)
    result = conn.execute(query).fetchall()
    print(result)

    # Retornar los resultados como una lista de diccionarios
    return [{"presion_sistolica": row.presion_sistolica, "presion_diastolica": row.presion_diastolica} for row in result]

@data_user.post("/data_user/{id}" , response_model=Data, tags=["data"])
def write_data_users(data: Data):
    dataContent = {"id_usuario": data.id_usuario, 
                   "presion_sistolica": data.presion_sistolica,
                   "presion_diastolica": data.presion_diastolica}
    result = conn.execute(mediciones_presion.insert().values(dataContent))

    data_id = result.inserted_primary_key[0]
    print(data_id)
    
    # Consulta el usuario creado usando el ID obtenido
    created_data = conn.execute(mediciones_presion.select().where(mediciones_presion.c.id == data_id)).mappings().first()
    conn.commit()
    
    return created_data if created_data else {"error": "data not found"}



