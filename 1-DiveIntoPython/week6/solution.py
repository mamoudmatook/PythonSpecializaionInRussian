import asyncio
metric_dics = dict()

def process_data( command):
    chunks = command.strip('\r\n').split()
    if not chunks:
        return 'error\nwrong command\n\n'
    if chunks[0] == 'get':
        if len(chunks) != 2:
            return 'error\nwrong command\n\n'
        return process_get(chunks[1])
    elif chunks[0] == 'put':
        if len(chunks) != 4:
            return 'error\nwrong command\n\n'
        return process_put(chunks[1], chunks[2], chunks[3])
    else:
        return 'error\nwrong command\n\n'

def process_get(key):
    res = 'ok\n'
    if key == '*':
        for key, values in metric_dics.items():
            for value in values:
                res = res + key + ' ' + value[1] + ' ' + value[0] + '\n'
    else:
        if key in metric_dics:
            for value in metric_dics[key]:
                res = res + key + ' ' + value[1] + ' ' + value[0] + '\n'

    return res + '\n'

def process_put(key, value, timestamp):
    try:
        timestamp = str(int(timestamp))
        value = str(float(value))
    except:
        return 'error\nwrong command\n\n'

    if key == '*':
        return 'error\nkey cannot contain *\n\n'
    if not key in metric_dics:
        metric_dics[key] = list()
    exist_time_stamp = False
    index = None
    for i, t in enumerate(metric_dics[key]):
        if t[0] == timestamp:
            exist_time_stamp = True
            index = i
            break 
    
    if exist_time_stamp:
        del metric_dics[key][index]
        
    metric_dics[key].append((timestamp, value))
    return 'ok\n\n'

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())


def run_server(address, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, address, port)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

# run_server('127.0.0.1', 10001)
