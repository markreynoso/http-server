# -*-coding=utf-8-*-
import socket
import sys


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5566))
    server.listen(1)
    print('connected')
    while True:
        try:
            conn, addr = server.accept()
            message = b''
            msg_recv = True
            while msg_recv:
                msg = conn.recv(8)
                message += msg
                if '|' in msg:
                    msg_recv = False
            conn.sendall(message)
            message = message[:(len(message) - 1)]
            print(message)
        except KeyboardInterrupt:
            print('Closing server')
            conn.shutdown(socket.SHUT_WR)
            conn.close()
            sys.exit(0)
