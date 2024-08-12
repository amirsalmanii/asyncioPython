"""
ex1 details of doing run function
"""
import asyncio
import time


async def main():
    print(f"{time.ctime()} started")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} closed")


loop = asyncio.get_event_loop()
task = loop.create_task(main())  # same tasks ++++++++++++++++++
loop.run_until_complete(task)   # when use this run all tasks
pending = asyncio.all_tasks(loop=loop) # same tasks ++++++++++++++++++

for task in pending:
    # if we have task in pending going to cancel
    # but all run_until_complete in up 
    # need to be commented to run this code block
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
