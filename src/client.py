import socket


def client(message):
    client = socket.socket(*socket.getaddrinfo('127.0.0.1', 5555)[1][:3])
    client.connect(('127.0.0.1', 5555))
    client.sendall(message.encode('utf-8'))

# if __name__ == '__main__':
