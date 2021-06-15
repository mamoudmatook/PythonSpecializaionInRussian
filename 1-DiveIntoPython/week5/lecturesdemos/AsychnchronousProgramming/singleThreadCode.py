import select
import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 1001))
sock.listen()
conn1, addr = sock.accept()
conn2, addr = sock.accept()
conn1.setblocking(0)
conn2.setblocking(0)
epoll = select.poll()
epoll.register(conn1.fileno(), select.POLLIN| select.POLLOUT)
epoll.register(conn2.fileno(), select.POLLIN| select.POLLOUT)
conn_map = {conn1.fileno(): conn1, conn2.fileno(): conn2}
while True:
    events = epoll.poll(1)
    for filno, event in events:
        if event &  select.POLLIN:
            data = conn_map[filno].recv(1024)
            print(data.decode('utf-8'))
        elif event & select.POLLOUT:
            conn_map[filno].send('ping'.encode('utf-8'))
