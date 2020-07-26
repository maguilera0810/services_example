import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
DATABASE_URL = "postgres://xkbtlxlccukuwo:302f0b16ae1b12ae20228b9da1e4f53997266514171d9eeab0d307f22097f79c@ec2-18-211-48-247.compute-1.amazonaws.com:5432/dammgs01fdoo32"
# database engine object from SQLAlchemy that manages connections to the database
engine = create_engine(DATABASE_URL)
# DATABASE_URL is an environment variable that indicates where the database lives
# create a 'scoped session' that ensures different users' interactions with the
db = scoped_session(sessionmaker(bind=engine))
# database are kept separate
db.execute(
    """CREATE TABLE t_categoria ( 
        id INTEGER PRIMARY KEY,
        nombre VARCHAR NOT NULL
        )"""
)
db.execute(
    """CREATE TABLE t_marca ( 
        id INTEGER PRIMARY KEY,
        nombre VARCHAR NOT NULL
        )"""
)
db.execute(
    """CREATE TABLE t_atributo ( 
        id INTEGER PRIMARY KEY,
        nombre VARCHAR NOT NULL
        )"""
)
db.execute(
    """CREATE TABLE t_valor ( 
        id INTEGER PRIMARY KEY,
        nombre VARCHAR NOT NULL
        )"""
)
db.execute(
    """CREATE TABLE t_producto ( 
        id INTEGER PRIMARY KEY,
        nombre VARCHAR NOT NULL,
        marca VARCHAR NOT NULL
        )"""
)
db.execute(
    """CREATE TABLE t_valor1_valor2_producto ( 
        id INTEGER PRIMARY KEY,
        val_1 INTEGER NOT NULL,
        val_2 INTEGER NOT NULL,
        id_prod INTEGER NOT NULL,
        precio FLOAT NOT NULL
        )"""
)


valores=["Camas","Salas"]
for idx,i in enumerate(valores):
    db.execute("INSERT INTO t_categoria (id,nombre) VALUES (:id,:nombre)",{"id":idx+1,"nombre":i})

valores =["Favenco","Chaide"]
for idx,i in enumerate(valores):
    db.execute("INSERT INTO t_marca (id,nombre) VALUES (:id,:nombre)",{"id":idx+1,"nombre":i})

valores =["Tipo","Tamaño"]
for idx,i in enumerate(valores):
    db.execute("INSERT INTO t_atributo (id,nombre) VALUES (:id,:nombre)",{"id":idx+1,"nombre":i})

valores =["Set","Colchon","King","Queen","Matrimonial","Imperial",]
for idx,i in enumerate(valores):
    db.execute("INSERT INTO t_valor (id,nombre) VALUES (:id,:nombre)",{"id":idx+1,"nombre":i})

valores = [
    ["Delva5","Favenco"],
    ["Basic2","Chaide"]
]
for idx,i in enumerate(valores):
    db.execute("INSERT INTO t_producto (id,nombre,marca) VALUES (:id,:nombre,:marca)",{"id":idx+1,"nombre":i[0],"marca":i[1]})



valores = [
    [1,3,1,500.0],
    [2,3,1,600.0],
    [1,4,1,700.0],
    [2,4,1,500.0],
    [1,5,1,600.0],
    [2,5,1,700.0],
    [1,6,1,400.0],
    [2,6,1,500.0],
    [1,3,2,600.0],
    [2,3,2,400.0],
    [1,4,2,700.0],
    [2,4,2,300.0]
]
for idx, i in enumerate(valores):
    db.execute("INSERT INTO t_valor1_valor2_producto (id,val_1,val_2,id_prod,precio) VALUES (:id,:val_1,:val_2,:id_prod,:precio)",{"id":idx+1,"val_1":i[0],"val_2":i[1],"id_prod":i[2],"precio":i[3]})


db.commit()

