from flask import Flask, request
from datetime import datetime
from flask_cors import CORS


# Esta variable __name__ es una variable propia de python que muestra si el archivo que estamos utilizando es el archivo principal del proyecto. Si es el archivo principal, su valor será __main__ caso contrario indicará otro valor.
app = Flask(__name__)

# La clase CORSsi solamente la pasamosla instancia muestra clase Flask entonces modificara los CORS para que puedan ser accedidos por todo el mundo (cualquier origen, cualquier metodo y cualquier cabecera)

CORS(app)

productos = []
devovlerProducto = []
# Enpoint
# Decorador es un patron de software que se utiliza para modificar un comportamiento de un metodo de una clase sin la necesidad de emplear otros metodos como la herencia, ademas tampoco es necesario modificar el comportamiento del metodo de dicha clase


@app.route("/")
def rutaInicial():
    print("Ingreso al endpoint inicial")
    return "Bienvenido a tu primera API de CodiGo :D"


@app.route("/estado")
def estadoAPI():
    return {
        "hora": datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    }


@app.route("/producto", methods=["POST"])
def gestionProductos():
    #  get_json() > convierte el json que el cliente envia a un diccionario para que python lo pueda entender.
    print(request.get_json())
    producto = request.get_json()
    productos.append(producto)
    return {
        "message": "Producto creado exitosamente",
        "content": producto
    }


@app.route("/devolver-producto", methods=["POST"])
def devolucionProducto():
    devProducto = request.get_json()
    devovlerProducto.append(devProducto)
    return {
        "message": "Producto devuelto exitosamente",
        "content": devProducto
    }
# crear un enpoint que seria /devolver-producto en el cual el frontend espera lo siguiente:
# {
#     "message" : "Los productos son",
#     "content" : "[{}]"
# }


# levantamos nuestro servidor para que se quede a la espera de posibles peticiones durante tiempo indeterminado hasta que manualmente se apague.
# debug > indicamos que si estamos en un servidor de prueba entonces cada vez que hagamos algun cambio a algun archivo del proyecto automaticamente se reiniciara el servidor agregando cambios (su valor por defecto es False)
app.run(debug=True)
