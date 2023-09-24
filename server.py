import socket
import random

def getRandomChoice():
    return random.randint(0, 3)

def main():
    LEDarray = [17,27,22,25]

    while True:
        computerChoice = getRandomChoice()
        sendCommand(client, LEDarray[computerChoice])