import socket

HOST = '127.0.0.1'  # localhost
PORT = 65432  # 自訂端口


def generate_guess_number():
    server_number = int(input("請輸入中獎號碼"))
    return server_number

def ultimate_password():
    pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode())
            conn.sendall(data)  # 回傳相同資料