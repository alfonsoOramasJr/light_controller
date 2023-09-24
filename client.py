import socket
import time
import gpiozero

def createClient():
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("CLIENT OK")
        return client

def getData(client):
        data = client.recv(1024).decode()
        while data == '':
                data = client.recv(1024).decode()
        return data

def sendData(client):
        message= "OK"
        client.send(message.encode())

def turnOff(GPIOpin):
        led = gpiozero.LED(GPIOpin)
        print("LED OFF")
        led.off()
        time.sleep(0.3)

def turnOn(GPIOpin):
        led = gpiozero.LED(GPIOpin)
        print("LED ON")
        led.on()
        time.sleep(0.3)

def execute(data):
        turnOff(data)
        turnOn(data)

def main():
        client = createClient()
        client.connect(('10.0.0.138', 3000))
        print("CONNETION OK")

        while True:
                sendData(client)
                data = getData(client)
                execute(data)
                data = ''

main()