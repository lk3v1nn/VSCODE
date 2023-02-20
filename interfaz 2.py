import requests

url = 'https://api.chat-api.com/666231808616863/sendMessage?token=EAAJd7y5KaZA8BAFTEZBoXhUbpaZBxnKnf1lmrgkauZBZAugpf4EgZBbKxkQuih6Hf6W74TbEPfKeWZAH1kvHLZCvZAYBkdmOmyfjyKGtjZBIl1NaSiERYorCSoWoViIA9AoTP4etW523ZCyXAvQNkM0fBAVRODCnQx9qasGRasdJYikImU027NL1165Hr1HFatz6kOu9ZCzcwdhengZDZD'
datos = {
    "phone": "50256327243",
    "body": "¡Hola! ¡Este es un mensaje de prueba enviado desde Python!"
}

respuesta = requests.post(url, json=datos)

print(respuesta.text)
