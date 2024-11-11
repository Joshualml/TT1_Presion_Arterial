from sqlalchemy import Table, Column, Integer, String, DECIMAL, ForeignKey, TIMESTAMP
from config.db import meta, engine
from sqlalchemy.sql import func

# Definición de la tabla 'usuarios'
usuarios = Table("usuarios", meta,
                Column("id", Integer, primary_key=True, autoincrement=True),  # AUTO_INCREMENT
                Column("nombre", String(100), nullable=False),
                Column("contraseña", String(255), nullable=False),
                Column("edad", Integer),
                Column("fecha_registro", TIMESTAMP, server_default=func.now())
                )  # Valor predeterminado a la fecha actual

# Definición de la tabla 'mediciones_presion'
mediciones_presion = Table("mediciones_presion", meta, 
                           Column("id", Integer, primary_key=True),
                           Column("id_usuario", Integer, ForeignKey("usuarios.id"), nullable=False),
                           Column("presion_sistolica", DECIMAL(5, 2), nullable=False),
                           Column("presion_diastolica", DECIMAL(5, 2), nullable=False),
                           Column("fecha_medicion", TIMESTAMP, server_default="CURRENT_TIMESTAMP")
                          )

# No es necesario ejecutar meta.create_all(engine) si las tablas ya existen en la base de datos
