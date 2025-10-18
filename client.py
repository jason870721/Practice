import socket

HOST = '127.0.0.1'
PORT = 65432

def input_guess_number():
    client_number = int(input("請輸入要猜測的號碼"))
    return client_number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, server!')
    data = s.recv(1024)

print('Received from server:', data.decode())