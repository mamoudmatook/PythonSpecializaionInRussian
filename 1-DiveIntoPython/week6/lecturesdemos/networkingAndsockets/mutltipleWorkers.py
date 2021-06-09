import threading
import socket
import multiprocessing
import os


def process_request(conn, addr):
    print("connected client ", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))


def worker(sock):
    while True:
        conn, addr = sock.accept()
        print("pid:", os.getpid())
        th = threading.Thread(target=process_request, args=(conn, addr))


with socket.socket() as sock:
    sock.bind(("127.0.0.1", 1001))
    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker, args=(sock,))]
    for w in workers_list:
        w.start()
    for w in workers_list:
        w.join()
