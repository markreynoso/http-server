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


def response_error(type):
    """Form a byte string for a 500 response."""
    return b'HTTP/1.1 {type} Internal server error \n <CRLF>\n'


def parse_request(message):
    """Parse the incoming request from client side"""
    message_list = message.decode('utf-8').split('<CRLF>')
    header_lines = message_[0].split('\n')
    request_line = header_lines.pop(0).split()

    if request_line[0] is 'GET' and request_line[2] is 'HTTP/1.1'
        response_ok()
    else:
        response_error(405)
    if check for header

    if none of the above, return URI of request.
        return request_list[1]

if __name__ == '__main__':  # pragma: no cover
    server()
