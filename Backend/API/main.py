import sys
from pathlib import Path

# Agrega la ruta del proyecto (un nivel arriba) a sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Dependencias
from raspberry.adquisicion import dataAdquisicion
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from API.routes.routers import routes 

origins = [
    "http://localhost:5173"
]

app = FastAPI(
    title="Presion Arterial UPIITA",
    description="CRUD de usuarios y sus mediciones de presion arterial",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "users routes",
        "name": "data",
        "description": "data routes"
    }]

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Incluir todas las rutas
for route in routes:
    app.include_router(route)

@app.get('/data')
def data_adquisition():
    data = dataAdquisicion()
    print(data)
    return data

