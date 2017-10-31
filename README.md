# http-server

## A simple server that echos back a message sent by the client. 

### server.py
    - Opens a socket that listens for hosts connections, takin in messages and echoing the messages back to the client.
    - Continues listening for client connections until keyboard interupt.

### client.py
    - Establishes a connection with server.py and sends a message over and waits for it to come back.
    - Once returned the client side closes.

#### use
    - To implement, run server.py to start server.
    - From command line, type request `python3 src/client.py 'your message'`