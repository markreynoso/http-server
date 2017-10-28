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
    server.bind(('127.0.0.1', 5637))
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
                message = response + '|'
                print(message)
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
    return 'HTTP/1.1 200 OK\n\r\n'


def response_error(type):
    """Form a string for a 500 response."""
    return 'HTTP/1.1 {}\nInternal server error\n\r\n\n'.format(type)


def parse_request(message):
    """Parse the incoming request from client side."""
    message_list = message.decode('utf-8').split('\r\n')
    # print(message_list)
    header_string = message_list[0]
    # print(header_string)
    host_string = message_list[1].replace('\n', '')
    # print(host_string)
    header_lines = header_string.split(' ')
    header = message_list[2].replace('\n', '')
    the_header = header.split(' ')
    # string_header_lines = header_lines.pop(0)
    host_line_list = host_string.split(' ')
    # print(host_line_list)
    # header_lines.pop()
    shl = " ".join(header_lines)
    # print(shl)
    valid_head = shl.split(' ')
    uri = valid_head[1]
    # print(uri)
    method = valid_head[0]
    # print(method)
    protocol = valid_head[2]
    # print(protocol)
    # valid_head = shl.split()
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
        ok = response_ok()
        uri = ok + '\n' + uri
        print(the_header)
        print(host_line_list[0])
        return uri
    elif method != 'GET' and protocol == 'HTTP/1.1':
        raise ValueError('405 Improper request method.')
    elif method == 'GET' and protocol != 'HTTP/1.1':
        raise ValueError('400 Improper protocol.')
    elif host_line_list[0] != 'Host:':
        raise ValueError('400 You must include Host:.')
    elif verified is False or len(the_header) == 0:
        print(the_header)
        raise ValueError('406 Improper header.')


if __name__ == '__main__':  # pragma: no cover
    server()
