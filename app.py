from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json

app = Flask(__name__)

DATABASE_URL = "postgres://xkbtlxlccukuwo:302f0b16ae1b12ae20228b9da1e4f53997266514171d9eeab0d307f22097f79c@ec2-18-211-48-247.compute-1.amazonaws.com:5432/dammgs01fdoo32"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(DATABASE_URL)

db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return ("Hola Giss, puedes usar el servicio distintas maneras si solo pondes '/producto/' te mostrará todos, los parametros siguientes son 'id_prod/val_1/val_2'")


@app.route("/producto/")
@app.route("/producto/<int:id_prod>")
@app.route("/producto/<int:id_prod>/<int:val1>")
@app.route("/producto/<int:id_prod>/<int:val1>/<int:val2>")
def api(id_prod="-1", val1="-1", val2="-1"):
    query = "SELECT * FROM t_valor1_valor2_producto"
    l = []
    if id_prod != "-1":
        l.append(f"id_prod = {id_prod}")
    if val1 != "-1":
        l.append(f"val_1 = {val1}")
    if val2 != "-1":
        l.append(f"val_2 = {val2}")

    if len(l) > 0:
        query += " WHERE " + " AND ".join(l)
    print(query)
    listado = db.execute(query).fetchall()

    yeison = {"productos": []}
    for i in listado:
        val_1 = db.execute(
            f"SELECT nombre FROM t_valor WHERE id = '{i[1]}'").fetchall()
        val_2 = db.execute(
            f"SELECT nombre FROM t_valor WHERE id = '{i[2]}'").fetchall()
        prod_name = db.execute(
            f"SELECT nombre FROM t_producto WHERE id = '{i[3]}'").fetchall()
        dic = {
            "id": i[0],
            "tipo": val_1[0][0],
            "tamano": val_2[0][0],
            "nombre": prod_name[0][0],
            "precio": i[4],
        }
        yeison["productos"].append(dic)
    print(yeison)
    status = 200
    if len(listado) == 0:
        status = 404
    return json.dumps(yeison), status


if __name__ == "__main__":
    app.run(debug=True)
