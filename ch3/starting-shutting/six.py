import asyncio
from signal import SIGINT, SIGTERM

##### Signal handling when using asyncio.run()


async def main():
    loop = asyncio.get_event_loop()
    for sig in (SIGINT,SIGTERM):
        loop.add_signal_handler(sig, handler, sig)

   
    try:
        while True:
            print("You Application is Running...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        for i in range(3):
            print("You Application is Shutting Down...")
            await asyncio.sleep(1)
            

def handler(sig):
    loop = asyncio.get_event_loop()
    
    for task in asyncio.all_tasks(loop=loop):
        task.cancel()
    
    print("Got Signal shutting down...")
    loop.remove_signal_handler(SIGTERM)
    loop.add_signal_handler(SIGINT,lambda: None)


if __name__ == "__main__":
    asyncio.run(main())
