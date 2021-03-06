import asyncio

async def tcp_echo_client(message, loop):
    reader , writer = await asyncio.open_connection('127.0.0.1', 1001, loop= loop)
    print('send message %r' % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()
message = 'hello world'
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()