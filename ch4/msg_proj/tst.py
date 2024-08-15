import asyncio

import time

async def main():
   reader, writer = await asyncio.open_connection(host="127.0.0.1", port="25000")

asyncio.run(main())