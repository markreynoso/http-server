# -*-coding=utf-8-*-
import socket


def client(message):
    message += '|'
    info = socket.getaddrinfo('127.0.0.1', 5566)
    stream = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream[:3])
    client.connect((stream[-1]))
    client.sendall(message.encode('utf-8'))
    message = ''
    msg_recv = True
    while msg_recv:
        msg = client.recv(8).decode('utf-8')
        message += msg
        if '|' in msg:
            msg_recv = False
    message = message[:(len(message) - 1)]
    print(message)
    client.close()
    return message
    

# if __name__ == '__main__':
