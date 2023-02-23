import requests
from requests.structures import CaseInsensitiveDict

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # decodificar el mensaje HTTP POST
        post_data = post_data.decode('utf-8')

        # analizar el contenido JSON del mensaje HTTP POST
        post_json = json.loads(post_data)

        # imprimir el contenido del mensaje HTTP POST
        print(f"Mensaje HTTP POST recibido: {post_json}")

        ######################
        # Envia el mensaje al whatsapp
        
        url = "https://graph.facebook.com/v15.0/101042539575372/messages"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer EAAJd7y5KaZA8BAN0t0ZC8VVVAhNzmtmpaESVrJlLEDwLwAqVCMg9z5ImZCWX1LLGCVOhDrbXM03VoE9oS2vrSWWbav5oRrw6djnVs1nPoWKZAT6IJSxPKsWuy697jPkfeLtq7PtQIj8VyjZCHZBoGUrjchZB3EmSosLdZAsfL5LelNV92DcVz653oN6RrRETjGQX3RMXCURxggZDZD"
        headers["Content-Type"] = "application/json"

        data = '{ "messaging_product": "whatsapp", "to": "50256327243", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }'


        resp = requests.post(url, headers=headers, data=data)

        print(resp.status_code)

        # enviar una respuesta al cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = "Mensaje HTTP POST recibido"
        self.wfile.write(response.encode('utf-8'))


def run_server():
    print("Ip: ")
    Ip_k = str(input())
    print("Puerto: ")
    Puerto_k = int(input())
    server_address = (Ip_k, Puerto_k)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f'Servidor en ejecución: http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()