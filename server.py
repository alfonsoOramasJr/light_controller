import socket
import random

def createServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

def getRandomChoice():
    return random.randint(0, 3)

def main():
    LEDarray = [17,27,22,25]

    while True:
        computerChoice = getRandomChoice()
        sendCommand(client, LEDarray[computerChoice])