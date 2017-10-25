# -*-coding=utf-8-*-
"""Create a socket on which a server will run."""
import socket


def server():
    """Create an open server to listen and echo message."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    server.bind(('127.0.0.1', 5570))
    server.listen(1)
    print('connected')
    try:
        while True:
            conn, addr = server.accept()
            message = b''
            msg_recv = True
            while msg_recv:
                msg = conn.recv(8)
                message += msg
                if b'|' in msg:
                    msg_recv = False
            message = message[:(len(message) - 1)]
            print(message.decode('utf-8'))
            message = message + '|'
            conn.sendall(message)
            conn.close()
    except KeyboardInterrupt:
        print('Closing server.')
        server.close()


if __name__ == '__main__':  # pragma: no cover
    server()
