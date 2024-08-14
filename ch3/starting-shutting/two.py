import asyncio
from asyncio import StreamReader, StreamWriter

##### Asyncio application life cycle (based on the TCP echo server in the Python documentation)


async def send_event(msg: str):
    await asyncio.sleep(1)


async def echo(reader: StreamReader, writer:StreamWriter):
    print("new connection")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("leaving connection")
    except asyncio.CancelledError:
        msg = "connection dropped!"
        asyncio.create_task(send_event(msg)) ## never do that because task destroy before done

async def main(host="127.0.0.1", port="8888"):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()



try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("bye!")