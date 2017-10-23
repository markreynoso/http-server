import socket


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5555))
    server.listen(1)
    conn, addr = server.accept()
    msg = ''
    while True:
        msg = msg + conn.recv(8)
        if len(conn.recv(8)) < 8:
            break
    print(msg)
