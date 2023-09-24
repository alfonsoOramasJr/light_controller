import socket

def getData():
    pass

def main():
    client = createClient()
    
    while True:
        data = getData()
        execute(data)