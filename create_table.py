#!/usr/bin/env python

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
import urllib.parse
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


database_name = 'erney'
username = 'erneypuetate'
password = 'Adolfo2008'
encoded_password = urllib.parse.quote_plus(password)

# Crear el URI de conexión
uri = f"postgresql://{username}:{password}@172.17.0.2/{database_name}"
engine = create_engine(uri)
# Define la tabla
metadata = MetaData(bind=engine)

tabla = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('email', String(50)),
              Column('password', String(50))
              )

# Verifica si la tabla existe antes de crearla
tabla.create()
engine.dispose()
print("La tabla ha sido creada.")

