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
    server.bind(('127.0.0.1', 5602))
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
            bar = b'|'
            response = parse_request(message)
            message = response + bar
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
    return 'HTTP/1.1 tpye Internal server error \n <CRLF>\n'


def parse_request(message):
    """Parse the incoming request from client side."""
    message_list = message.decode('utf-8').split('<CRLF>')
    print(message_list)
    header_string = message_list[0]
    print(header_string)
    header_lines = header_string.split('\\n')
    print(header_lines)
    string_header_lines = header_lines.pop(0)
    print(string_header_lines)
    header_lines.pop()
    print(header_lines)
    shl = " ".join(header_lines)
    print(shl)
    request_line = string_header_lines.split()
    print(request_line)
    uri = request_line[1].encode('utf-8')
    print(uri)
    method = request_line[0]
    print(method)
    protocol = request_line[2]
    print(protocol)
    valid_head = shl.split()
    print(valid_head)
    correct = 0
    verified = False
    for i in range(len(valid_head)):
        if(i % 2 == 0):
            if ':' in valid_head[i]:
                correct += 1
        else:
            if len(valid_head[i]) > 0:
                correct += 1
    if (len(valid_head) == correct and len(valid_head) % 2 == 0):
        verified = True
    if method == 'GET' and protocol == 'HTTP/1.1' and len(header_lines) > 0\
            and verified:
        ok = response_ok()
        print(type(ok))
        print(type(uri))
        uri = ok + b'\n' + uri
        print(uri)
        print(type(uri))
        return uri
    elif method is not 'GET' and protocol is 'HTTP/1.1':
        error_val = response_error(405)
        return error_val
    elif method is not 'GET' and protocol is not 'HTTP/1.1':
        error_val = response_error(400)
        return error_val
    elif verified is False or len(header_lines) == 0:
        error_val = response_error(406)
        return error_val


if __name__ == '__main__':  # pragma: no cover
    server()
