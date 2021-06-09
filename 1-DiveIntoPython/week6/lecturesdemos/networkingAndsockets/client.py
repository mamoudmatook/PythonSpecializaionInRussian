import socket
with socket.socket() as sock:
    sock.connect(('127.0.0.1', 1001))
    while True:
        sock.sendall("ping2".encode('utf-8'))