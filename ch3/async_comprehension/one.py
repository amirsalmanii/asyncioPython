import asyncio


async def doubler(n):
    for i in range(n):
        yield i, i*2
        await asyncio.sleep(3)
# total 27 sec

"""
my useful view

async def doubler(n):
    ta = []
    for i in range(n):
        yield i, i*2
        ta.append(asyncio.sleep(3))
    await asyncio.gather(*ta)   

    
total 9 sec
"""

    
async def main():
    result = [x async for x in doubler(3)] # async list comprehension
    print(result)

    result = {x: y async for x, y in doubler(3)} # async dict comprehension
    print(result)

    result = {x async for x in doubler(3)} # async set comprehension
    print(result)

asyncio.run(main())


import asyncio
