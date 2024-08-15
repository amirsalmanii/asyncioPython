import time
import asyncio

# note this problem for python 3.8 and under   3.9 adn above fixed
##### The executor takes too long to finish
#problem:
async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')

def blocking():
    time.sleep(1.5)
    print(f"{time.ctime()} Hello from a thread!")

asyncio.run(main())


# solution:
###### Option A: wrap the executor call inside a coroutine
async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    try:
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')
    finally:
        await future

def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread!")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Bye!')