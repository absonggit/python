import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('10.10.20.28',1234))

server.listen()
print("服务启动成功")
clineSocket, clinetAddress = server.accept()
while True:
    data = clineSocket.recv(1024)
    print(str(clinetAddress) + ":" + data.decode("utf-8"))
server.close()