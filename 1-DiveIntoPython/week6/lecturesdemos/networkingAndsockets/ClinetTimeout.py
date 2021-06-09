import socket
with socket.create_connection(('127.0.0.1', 1001), 5) as sock:
    sock.settimeout(2)
    try:
        while True:
            sock.sendall('ping'.encode('utf-8'))
    except socket.timeout:
        print('send data tiemout')
    except socket.error as ex:
        print('send data error ' , ex)
    