import socket


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5555))
    server.listen(1)
    conn, addr = server.accept()
    message = ''
    while True:
        msg = conn.recv(8)
        message += msg
        if len(msg) < 8:
            break
    print(message)
