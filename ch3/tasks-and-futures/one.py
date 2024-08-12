import asyncio

###### Interaction with a Future instance
async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    f.set_result("my task is down")


def check_future_status_results(f: asyncio.Future):
    print(f"future is done? {f.done()}")
    print(f"future is cancelled? {f.cancelled()}")
    try:
        print(f"future result is: {f.result()}")
    except asyncio.exceptions.InvalidStateError as e:
        pass
    except asyncio.exceptions.CancelledError:
        pass


fu = asyncio.Future()

check_future_status_results(fu)

loop = asyncio.get_event_loop()

result1 = loop.create_task(main(f=fu))

print(result1)

loop.run_until_complete(result1) # on a Future instance, rather than a Task instance

check_future_status_results(fu)

"""
easy api solution
fu = asyncio.Future()

check_future_status_results(fu)

asyncio.run(main(f=fu))

check_future_status_results(fu)
"""

###### Calling set_result() on a Task
print("####"*12)

async def main(f: asyncio.Future):
    await asyncio.sleep(1)
    try:
        f.set_result("complete task!")
    except RuntimeError as e:
        print("NOT lONGER SUPPORT {e}")
        f.cancel()
    
loop = asyncio.get_event_loop()

fut = asyncio.Task(asyncio.sleep(1_000_000))

check_future_status_results(f=fut)

t1 = loop.create_task(main(f=fut))

loop.run_until_complete(t1)

check_future_status_results(f=fut)
