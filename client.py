import socket

def createClient():
    pass

def getData(client):
    pass

def main():
    client = createClient()

    while True:
        data = getData(client)
        execute(data)