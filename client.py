import socket

def createClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client

def getData(client):
    pass

def main():
    client = createClient()
    client.connect(('10.0.0.138', 3000))

    while True:
        data = getData(client)
        execute(data)