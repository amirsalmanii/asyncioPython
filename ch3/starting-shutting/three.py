import asyncio

# What Is the return_exceptions=True for in gather()?
# All the tasks will complete


async def f(delay:int):
    await asyncio.sleep(1/delay)
    return delay


loop = asyncio.get_event_loop()

for delay in range(10):
    loop.create_task(f(delay))

pending = asyncio.all_tasks(loop)


gp = asyncio.gather(*pending, return_exceptions=True) # in this situation just return exception in result like str and rest of task done
#gp = asyncio.gather(*pending) # in this situation raise ZeroDivisionError and dont allow the rest of tasks done

results = loop.run_until_complete(gp)

print(f"Results: {results}")
loop.close()