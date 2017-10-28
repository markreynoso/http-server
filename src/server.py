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
    server.bind(('127.0.0.1', 5671))
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
                    body, size, f_type = resolve_uri(response)
                    message = body + str(size) + f_type + '|'
                    conn.sendall(message.encode('utf-8'))
                except ValueError as back:
                    error_msg = response_error(back)
                    message = error_msg + '|'
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
        sys.exit(0)


def response_ok():
    """Form a string for a 200 connection."""
    return 'HTTP/1.1 200 OK\n\r\n'


def response_error(type):
    """Form a string for a 500 response."""
    return 'HTTP/1.1 {}\nInternal server error\n\r\n\n'.format(type)


def parse_request(message):
    """Parse the incoming request from client side."""
    message_list = message.decode('utf-8').split('\r\n')
    header_string = message_list[0].split('\n')
    host_string = header_string[1]
    the_header = header_string[2].split(' ')
    host_line_list = host_string.split(' ')
    valid_head = header_string[0].split(' ')
    uri = valid_head[1]
    method = valid_head[0]
    protocol = valid_head[2]
    correct = 0
    verified = False
    for i in range(len(the_header)):
        if(i % 2 == 0):
            if ':' in the_header[i]:
                correct += 1
        else:
            if len(the_header[i]) > 0:
                correct += 1
    if len(the_header) == correct and len(the_header) % 2 == 0:
        verified = True
    if method == 'GET' and protocol == 'HTTP/1.1' and len(the_header) > 0\
            and verified and host_line_list[0] == 'Host:':
        # ok = response_ok()
        # uri = ok + '\n' + uri
        return uri
    elif method != 'GET' and protocol == 'HTTP/1.1':
        raise ValueError('405 Improper request method.')
    elif method == 'GET' and protocol != 'HTTP/1.1':
        raise ValueError('400 Improper protocol.')
    elif host_line_list[0] != 'Host:':
        raise ValueError('400 You must include Host:.')
    elif verified is False or len(the_header) == 0:
        raise ValueError('406 Improper header.')


def resolve_uri(uri):
    """Handle file requests."""
    path = '/'.join([os.path.dirname(os.path.abspath(__file__)),
                     'webroot', uri]).replace('//', '/')
    if os.path.exists(path):
        if os.path.isfile(path):
            with open(path, 'rb') as text:
                body = text.read()
            size = len(body)
            f_type = guess_type(path)
            return body, size, f_type[0]
        elif os.path.isdir(path):
            dir_list = ''
            for item in os.listdir(path):
                dir_list += item + '\n'
            return '<html><body>{}<body/><html/>'.format(dir_list)
    else:
        raise ValueError('404 Need authorization.')


if __name__ == '__main__':  # pragma: no cover
    server()
