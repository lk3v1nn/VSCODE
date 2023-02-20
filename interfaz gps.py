from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recibir_solicitud():
  # Obtener los datos de la solicitud POST HTML
  datos = request.form['datos']

  # Configurar el comando cURL
  url = 'http://ejemplo.com'
  headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  datos_curl = {'datos': datos}

  # Ejecutar el comando cURL
  respuesta = requests.post(url, headers=headers, data=datos_curl)

  # Retornar la respuesta
  return respuesta.text
