import socket
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 1001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        conn.settimeout(5)
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print('close connectiong by timeout')
                    break
                if not data:
                    break
                print(data.decode('utf-8'))