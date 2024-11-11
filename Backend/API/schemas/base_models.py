from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    nombre: str
    contraseña: str
    edad: int

class UserCreate(UserBase):
    pass  # Usado solo para creación, sin `id` ni `fecha_registro`

class User(UserBase):
    id: Optional[int]
    fecha_registro: Optional[datetime]

class Data(BaseModel):
    id: Optional[int]
    id_usuario: int
    presion_sistolica: float
    presion_diastolica: float
    fecha_medicion: Optional[datetime]

class DataPressure(BaseModel):
    presion_sistolica: float
    presion_diastolica: float