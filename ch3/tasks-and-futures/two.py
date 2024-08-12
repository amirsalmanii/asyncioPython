import asyncio

##### ensure_future()
"""
ensure_future use by framework designers
because accept task and coro without error
when get task return without modification
when get coro act like create task and scheduled on event loop
"""
async def f():
    pass


coro = f()

loop = asyncio.get_event_loop()

task = loop.create_task(coro) # same
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro) # same
assert isinstance(new_task, asyncio.Task)

mystery_meat = asyncio.ensure_future(task) # get task and return task without modification
assert mystery_meat is task