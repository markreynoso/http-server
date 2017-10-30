# -*-coding=utf-8-*-
"""Create a socket on which a server will run."""
import sys
from gevent.server import StreamServer
from gevent.monkey import patch_all
from server import response_ok, response_error, parse_request, resolve_uri


def server():  # pragma: no cover
    """Create an open server to listen and echo message."""
    try:
        patch_all()
        server = StreamServer(('127.0.0.1', 6001), echo)
        print('connected')
        server.serve_forever()

    except KeyboardInterrupt:
        print('Closing server.')
        server.close()
        sys.exit(0)


def echo(socket, addr):  # pragma: no cover
    """Receive and return client messages."""
    while True:
        message = b''
        msg_recv = True
        while msg_recv:
            msg = socket.recv(8)
            message += msg
            if b'|' in msg:
                msg_recv = False
        message = message[:(len(message) - 1)]
        try:
            response = parse_request(message)
            try:
                return_search = resolve_uri(response)
                ok = response_ok(return_search)
                message = ok + '|'
                socket.sendall(message.encode('utf-8'))
            except ValueError as back:
                error_msg = response_error(back)
                message = error_msg + '|'
                socket.sendall(message.encode('utf-8'))
        except ValueError as back:
            error_msg = response_error(back)
            message = error_msg + '|'
            socket.sendall(message.encode('utf-8'))
        socket.close()


if __name__ == '__main__':  # pragma: no cover
    server()
