from flask import Flask, render_template, request
import numpy as np
from statistics import mode, median, variance, stdev

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    # Obtener los datos del formulario
    datos = request.form.get("datos")
    
    # Convertir los datos a una lista de números
    try:
        datos = [float(x) for x in datos.split(",")]
    except ValueError:
        return "Error: Ingresa números separados por comas."

    # Calcular las métricas
    media = np.mean(datos)
    moda = mode(datos)
    mediana = median(datos)
    varianza = variance(datos)
    desviacion_estandar = stdev(datos)

    # Pasar los resultados a la plantilla
    return render_template("resultados.html", 
                           media=media, 
                           moda=moda, 
                           mediana=mediana, 
                           varianza=varianza, 
                           desviacion_estandar=desviacion_estandar)

if __name__ == "__main__":
    app.run(debug=True)