import socket

def createClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("CLIENT OK")
    return client

def getData(client):
    data = client.recv(1024).decode()

def main():
    client = createClient()
    client.connect(('10.0.0.138', 3000))
    print("CONNECTION OK")

    while True:
        data = getData(client)
        execute(data)