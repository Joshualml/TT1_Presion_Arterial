from fastapi import APIRouter
from models.db import usuarios
from config.db import conn
from config.db import f
from API.schemas.base_models import User, UserCreate
from fastapi import HTTPException


users = APIRouter()

@users.get('/login', response_model=list[User], tags=["users"])
def get_user():
    return conn.execute(usuarios.select()).mappings().fetchall()


@users.post('/register', response_model=User, tags=["users"])
def register_user(user: UserCreate):
    try:
        new_user = {"nombre": user.nombre, "edad": user.edad}
        new_user["contraseña"] = f.encrypt(user.contraseña.encode("utf-8"))
        result = conn.execute(usuarios.insert().values(new_user))
        user_id = result.inserted_primary_key[0]

        created_user = conn.execute(usuarios.select().where(usuarios.c.id == user_id)).mappings().first()
        conn.commit()
        return created_user if created_user else {"error": "User not found"}

    except Exception as e:
        print("Error al registrar usuario:", e)
        raise HTTPException(status_code=422, detail=str(e))

