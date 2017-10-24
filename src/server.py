import socket
import sys


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5558))
    server.listen(1)
    print('connected')
    while True:
        try:
            conn, addr = server.accept()
            message = ''
            msg_recv = True
            while msg_recv:
                msg = conn.recv(8)
                message += msg
                if len(msg) < 8:
                    msg_recv = False
            conn.sendall(message)
            print(message)
        except KeyboardInterrupt:
            print('Closing server')
            conn.shutdown(socket.SHUT_WR)
            conn.close()
            sys.exit(0)
