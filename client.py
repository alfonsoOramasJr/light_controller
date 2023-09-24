import socket
import time

def createClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("CLIENT OK")
    return client

def getData(client):
    data = client.recv(1024).decode()

def turnOffLED(data):
    pass

def turnOnLED(data):
    pass

def execute(data):
    turnOffLED(data)
    time.sleep(1)
    turnOnLED(data)

def main():
    client = createClient()
    client.connect(('10.0.0.138', 3000))
    print("CONNECTION OK")

    while True:
        data = getData(client)
        execute(data)