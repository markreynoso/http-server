# -*-coding=utf-8-*-
"""Create a socket on which a server will run."""
import socket
import io
import os


def server():
    """Create an open server to listen and echo message."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    server.bind(('127.0.0.1', 5691))
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
            try:
                response = parse_request(message)
                ok = response_ok()
                message = ok + response + '|'
                conn.sendall(message.encode('utf-8'))
            except ValueError as back:
                error_msg = response_error(back)
                message = error_msg + '|'
                print(message)
                conn.sendall(message.encode('utf-8'))
            conn.close()
    except KeyboardInterrupt:
        print('Closing server.')
        server.close()


def response_ok():
    """Form a string for a 200 connection."""
    return 'HTTP/1.1 200 OK\r\n\n'


def response_error(type):
    """Form a string for a 500 response."""
    return 'HTTP/1.1 {}\nInternal server error\n\r\n\n'.format(type)


def parse_request(message):
    """Parse the incoming request from client side."""
    message_list = message.decode('utf-8').split('\r\n')
    header_string = message_list[0]
    host_string = message_list[1].replace('\n', '')
    valid_head = header_string.split(' ')
    host_line_list = host_string.split(' ')
    uri = valid_head[1]
    method = valid_head[0]
    protocol = valid_head[2].replace('\n', '')
    if method == 'GET' and protocol == 'HTTP/1.1' and\
       host_line_list[0] == 'Host:' and len(host_line_list[1]) > 0:
        return uri
    elif method != 'GET' and protocol == 'HTTP/1.1':
        raise ValueError('405 Improper request method.')
    elif method == 'GET' and protocol != 'HTTP/1.1':
        raise ValueError('400 Improper protocol.')
    elif host_line_list[0] != 'Host:':
        raise ValueError('400 You must include Host:.')
    elif len(host_line_list[1]) == 0:
        raise ValueError('406 Improper header.')


if __name__ == '__main__':  # pragma: no cover
    server()
