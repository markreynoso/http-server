# -*-coding=utf-8-*-
"""Create a socket on which a server will run."""
import socket
import sys
import os
from mimetypes import guess_type

def server():
    """Create an open server to listen and echo message."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    server.bind(('127.0.0.1', 5689))
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
                try:
                    return_search = resolve_uri(response)
                    ok = response_ok(return_search)
                    message = ok + '|'
                    conn.sendall(message.encode('utf-8'))
                except ValueError as back:
                    error_msg = response_error(back)
                    message = error_msg + '|'
                    conn.sendall(message.encode('utf-8'))
            except ValueError as back:
                error_msg = response_error(back)
                message = error_msg + '|'
                conn.sendall(message.encode('utf-8'))
            conn.close()
    except KeyboardInterrupt:
        print('Closing server.')
        server.close()
        sys.exit(0)


def response_ok(return_search):
    """Form a string for a 200 connection."""
    return 'HTTP/1.1 200 OK\n{}'.format(return_search)


def response_error(type):
    """Form a string for a 500 response."""
    return 'HTTP/1.1 {}\nInternal server error\n'.format(type)


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


def resolve_uri(uri):
    """Handle file requests."""
    if uri.startswith('..'):
        raise ValueError('403 Access denied.')
    path = '/'.join([os.path.dirname(os.path.realpath(__file__)),
                     'webroot', uri]).replace('//', '/')
    if os.path.exists(path):
        if os.path.isfile(path):
            with open(path) as text:
                body = text.read()
            size = len(body)
            f_type = guess_type(path)
            output = ('Content-Type: {}\n'
                      'Length: {}\n\r\n'
                      'Body:\n{}'.format(f_type, str(size), body))
            return output
        elif os.path.isdir(path):
            dir_list = ''
            length = 0
            for item in os.listdir(path):
                dir_list += item + '\n'
                length += 1
            return ('Content-Type: directory\n'
                    'Number-of-files: {}\n\r\n'
                    '<html><body>{}<body/><html/>'.format(length, dir_list))
    else:
        raise ValueError('400 File does not exist.')


if __name__ == '__main__':  # pragma: no cover
    server()
