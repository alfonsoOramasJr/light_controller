import socket

def createClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def getData(client):
    pass

def main():
    client = createClient()

    while True:
        data = getData(client)
        execute(data)