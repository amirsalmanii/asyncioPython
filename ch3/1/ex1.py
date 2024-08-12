import asyncio
import time


async def main():
    print(f"{time.ctime()} started")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} closed")


asyncio.run(main())


"""
just my view:

import asyncio
import time

async def another_task():
    print(f"{time.ctime()} another_task started")
    await asyncio.sleep(5)  # Simulate a task that takes 2 seconds to complete
    print(f"{time.ctime()} another_task completed")

async def main():
    print(f"{time.ctime()} main started")
    
    # Start another_task concurrently
    task = asyncio.create_task(another_task())
    
    await asyncio.sleep(1)  # main function is blocked for 1 second
    print(f"{time.ctime()} main continuing")
    
    # Wait for another_task to complete
    await task
    
    print(f"{time.ctime()} main closed")

# Run the event loop
asyncio.run(main())

"""