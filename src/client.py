# -*-coding=utf-8-*-
"""Create a socket on which a client will run."""
import socket
import sys


def client(message):
    """Create an client to send and receive message."""
    message += '|'
    info = socket.getaddrinfo('127.0.0.1', 5602)
    stream = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream[:3])
    client.connect((stream[-1]))
    if sys.version_info.major == 3:
        client.sendall(message.encode('utf-8'))
    else:
        client.sendall(message)
    message = b''
    msg_recv = True
    while msg_recv:
        msg = client.recv(8)
        message += msg
        if b'|' in msg:
            msg_recv = False
    message = message.decode('utf-8')
    message = message[:(len(message) - 1)]
    client.close()
    return message


if __name__ == '__main__':  # pragma: no cover
    message = sys.argv[1]
    print(client(message))
