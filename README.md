# http-server

##server.py
    - Opens a socket that listens for hosts connections, takin in messages and echoing the messages back to the client.
    - Continues listening for client connections until keyboard interupt.
    - Adds a byte string to return messages with the response code.
    - Receives only GET requests via HTTP/1.1. Requests must come with a valid header. Improper request will raise error.

##client.py
    - Establishes a connection with server.py and sends a message over and waits for it to come back.
    - Once returned the client side closes.