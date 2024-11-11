import os
from sqlalchemy import create_engine, MetaData
from cryptography.fernet import Fernet

# Configuración de la base de datos
engine = create_engine("mysql+pymysql://root:Energy.Lost99frAm3@localhost:3306/presiona_IPN")
meta = MetaData()
conn = engine.connect()

# Configuración de la clave de cifrado
SECRET_KEY = os.getenv("SECRET_KEY", Fernet.generate_key())  # Genera la clave si no está en variables de entorno
f = Fernet(SECRET_KEY)  # Instancia de Fernet para cifrar y descifrar
