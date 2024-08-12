import asyncio


class Connection:
    def __init__(self, host: int, port: int) -> None:
        self.host = host
        self.port = port

    async def __aenter__(self):
        self.conn = await self.get_conn(self.host, self.port)

    async def __aexit__(self, exc_type, exc, tb):
        self.conn.close()

    async def get_conn(self, host, port):
        print(f"connection opening on {host}:{port}")
        print()
        await asyncio.sleep(0.5)
        return self

    def close(self):
        print()
        print("connection closed!")


async def main():
    async with Connection("127.0.0.1", "5432") as cn:
        print("doing some jobs with connection class")


asyncio.run(main())
