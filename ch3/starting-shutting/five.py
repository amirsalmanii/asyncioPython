import asyncio
from signal import SIGINT, SIGTERM

##### Handle both SIGINT and SIGTERM, but stop the loop only once

async def main():
    try:
        while True:
            print('<Your app is running>')
            await asyncio.sleep(1)
    except asyncio.CancelledError: # first run line 43 then here
        for i in range(3):
            print('<Your app is shutting down...>')
            await asyncio.sleep(1)

def handler(sig):
    loop.stop()
    print(f'Got signal: {sig!s}, shutting down.')
    loop.remove_signal_handler(SIGTERM)
    loop.add_signal_handler(SIGINT, lambda: None)  # send new signal dont allow do any think


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for sig in (SIGTERM, SIGINT):
        loop.add_signal_handler(sig, handler, sig)
    
    loop.create_task(main())

    print()
    print("run forever started...")
    print()
    #note: if you doesn't send any signal we are block here and never exe line 31  and rest
    loop.run_forever()
    #note: after send sig run the rest of code
    print()
    print("run rest code after send sig...")
    print()

    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group) # and then because you complete task to be cancel you send CancelledError in main coro then raise exception
    loop.close()