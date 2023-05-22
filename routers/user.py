from fastapi import APIRouter, Response, status
from config.db import table_users, engine
from schemas.user import userentity, usersentity
from models.user import User
from passlib.hash import sha256_crypt
#from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import create_engine, MetaData, Table, select

user=APIRouter()

@user.get('/users', response_model=list[User], tags=["users"])
def fidn_all_user():
    consulta = select([table_users])

    with engine.connect() as conn:
        resultados = conn.execute(consulta).fetchall()
    
    return usersentity(resultados)


   
@user.post('/users', response_model=User, tags=["users"])
def create_user(user:User):
    new_user = dict(user)
    #new_user["password"]=sha256_crypt.encrypt(new_user["password"])
    #del new_user["id"]
    id= new_user["id"]

    with engine.connect() as conn:
        conn.execute(table_users.insert().values(**new_user))

    criterio_busqueda = table_users.c.id == int(id)
    consulta = select([table_users]).where(criterio_busqueda)
    with engine.connect() as conn:
        resultados = conn.execute(consulta).fetchall()
        


    return userentity(resultados)



@user.get('/users/{id}', response_model=User, tags=["users"])
def find_user(id:str):

   
    criterio_busqueda = table_users.c.id == int(id)


    consulta = select([table_users]).where(criterio_busqueda)


    with engine.connect() as conn:
        resultados = conn.execute(consulta).fetchall()

        

    return userentity(resultados)



@user.put('/users/{id}', response_model=User, tags=["users"])
def update_user(id:str, user:User):
    new_user=dict(user)
    del new_user["id"]


    criterio_actualizacion = table_users.c.id == int(id)
    with engine.connect() as conn:
        conn.execute(table_users.update().values(**new_user).where(criterio_actualizacion))

    criterio_busqueda = table_users.c.id == int(id)
    consulta = select([table_users]).where(criterio_busqueda)
    with engine.connect() as conn:
        resultados = conn.execute(consulta).fetchall()
    
    return userentity(resultados)



@user.delete('/users/{id}', status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delate_user(id:str):

    criterio_eliminacion = table_users.c.id == int(id)
    with engine.connect() as conn:
        conn.execute(table_users.delete().where(criterio_eliminacion))
  
    return Response(status_code=HTTP_204_NO_CONTENT)
