import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("10.10.20.28", 1234))
while True:
    data = input()
    client.send(data.encode("utf-8"))
client.close()