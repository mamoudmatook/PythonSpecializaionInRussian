import socket
import time

class ClientError(Exception):
    pass

class Client:
    def __init__(self, ip, port, timeout = None):
        self.sock = socket.create_connection((ip, port), timeout)
    
    def __del__(self):
        self.sock.close()

    def send(self, messsage):
        self.sock.sendall(messsage.encode('utf-8'))
        return self.sock.recv(1024).decode('utf-8')
    
    def get(self, key):
        def process_entry(entry):
            try:
                key, value, timestamp = entry.split()
                if key in to_ret:
                    to_ret[key].append((int(timestamp), float(value)))
                else:
                    to_ret[key] = [(int(timestamp), float(value))]
            except:
                raise ClientError(resp)
            
        formatted_message = 'get {}\n'.format(key)
        resp = self.send(formatted_message)
        if resp[0:3] != 'ok\n':
            raise ClientError(resp)
        to_ret = {}
        enteris = resp.split('\n')
        for entry in enteris[1:-2]:
            process_entry(entry)
        for key in to_ret:
            to_ret[key] = sorted(to_ret[key])
        return to_ret

    def put(self, metric_name, value, timestamp = None):
        formatted_message = 'put {} {} {}\n'.format(metric_name, str(value), str(timestamp if timestamp else int(time.time())))
        resp = self.send(formatted_message)
        if  resp[0:3] != 'ok\n':
            raise ClientError(resp)