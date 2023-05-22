from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
#import urllib.parse
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# Crea una instancia del motor de SQLAlchemy
database_name = 'erney'
username = 'erneypuetate'
password = 'Adolfo2008'
#encoded_password = urllib.parse.quote_plus(password)

# Crear el URI de conexión
uri = f'postgresql://{username}:{password}@postgres:5432/erney'
engine = create_engine(uri)

# Define la tabla
metadata = MetaData(bind=engine)

table_users = Table('users', metadata, autoload=True)