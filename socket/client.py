import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Host: ")
port = int(input("Port: "))

client.connect((host, port))

while True:

    mesaj = "{lyk}"

    if mesaj == '{lyk}':
        while True:
            client.send(mesaj.encode('utf-8'))


client.close()