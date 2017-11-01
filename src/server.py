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
            ok = response_ok()
            message = ok + message + '|'
            conn.sendall(message)
            conn.close()
    except KeyboardInterrupt:
        print('Closing server.')
        server.close()


def response_ok():
    """Form a byte string for a 200 connection."""
    return b'HTTP/1.1 200 OK \n <CRLF>\n'


def response_error():
    """Form a byte string for a 500 response."""
    return b'HTTP/1.1 500 Internal server error \n <CRLF>\n'


if __name__ == '__main__':  # pragma: no cover
    server()
