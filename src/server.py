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
    server.bind(('127.0.0.1', 5622))
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
            # print(message.decode('utf-8'))
            try:
                response = parse_request(message)
                message = response + '|'
                conn.sendall(message.encode('utf-8'))
            except ValueError as back:
                error_msg = response_error(back)
                message = error_msg + '|'
                conn.sendall(message.encode('utf-8'))
            conn.close()
    except KeyboardInterrupt:
        print('Closing server.')
        server.close()


def response_ok():
    """Form a string for a 200 connection."""
    return 'HTTP/1.1 200 OK\n\r\n\n'


def response_error(type):
    """Form a string for a 500 response."""
    return 'HTTP/1.1 {}\nInternal server error\n\r\n\n'.format(type)


def parse_request(message):
    """Parse the incoming request from client side."""
    message_list = message.decode('utf-8').split('\r\n')
    header_string = message_list[0]
    header_lines = header_string.split('\n')
    string_header_lines = header_lines.pop(0)
    header_lines.pop()
    shl = " ".join(header_lines)
    request_line = string_header_lines.split()
    uri = request_line[1]
    method = request_line[0]
    protocol = request_line[2]
    valid_head = shl.split()
    correct = 0
    verified = False
    for i in range(len(valid_head)):
        if(i % 2 == 0):
            if ':' in valid_head[i]:
                correct += 1
        else:
            if len(valid_head[i]) > 0:
                correct += 1
    if len(valid_head) == correct and len(valid_head) % 2 == 0:
        verified = True
    if method == 'GET' and protocol == 'HTTP/1.1' and len(header_lines) > 0\
            and verified:
        ok = response_ok()
        uri = ok + '\n' + uri
        return uri
    elif method != 'GET' and protocol == 'HTTP/1.1':
        raise ValueError('405 Improper request method.')
        # error_val = response_error('405')
        # return error_val
    elif method == 'GET' and protocol != 'HTTP/1.1':
        raise ValueError('400 Improper protocol.')
        # error_val = response_error('400')
        # return error_val
    elif verified is False or len(header_lines) == 0:
        raise ValueError('406 Improper header.')
        # error_val = response_error('406')
        # return error_val


if __name__ == '__main__':  # pragma: no cover
    server()
