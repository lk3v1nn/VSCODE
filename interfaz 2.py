import requests

url = 'https://api.chat-api.com/101042539575372/sendMessage?token=EAAJd7y5KaZA8BAME1o6zoF8JSlQVrgBU2kyxSia7rrXAtCYRM1CZCvZCH2yw5R3ZCfHZBZAY7qf1fxCQ675ALLGHYL7tsNGjFygykPghv4nE6pQMNGBglexrbWkDaddtFvZCWtGTaXNvJvIgd5fVRfPVbBdCvclMVSz9XW8chwT7JkSQX5IsjRr4HE4ZCLfYfAymCbyaSD5evAZDZD'
datos = {
    "phone": "50256327243",
    "body": "¡Hola! ¡Este es un mensaje de prueba enviado desde Python!"
}

respuesta = requests.post(url, json=datos)

print(respuesta.text)
