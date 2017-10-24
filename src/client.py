import socket


def client(message):
    info = socket.getaddrinfo('127.0.0.1', 5558)
    stream = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream[:3])
    client.connect((stream[-1]))
    client.sendall(message.encode('utf-8'))
    message = ''
    msg_recv = True
    while msg_recv:
        msg = client.recv(8)
        message += msg
        if len(msg) < 8:
            msg_recv = False
    print(message)
    client.close()
    

# if __name__ == '__main__':
