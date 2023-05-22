from models.user import User
def userentity(item)-> dict:
    item = [User(id=resultado[0], name=resultado[1], email=resultado[2], password=resultado[3]) for resultado in item]

    return {
        "id": item[0].id,
        "name": item[0].name,
        "email": item[0].email,
        "password": item[0].password
        
    }

def usersentity(entity)-> list:
    #return [userentity(item) for item in entity]
    return entity