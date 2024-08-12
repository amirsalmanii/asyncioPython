import asyncio


async def f():
    return 111


# on evaluation turn to continue
print(type(f)) # function
print(type(f())) # continue


##### behind since loops
print("######" * 12)
coro = f()
try:
    coro.send(None)
except StopIteration as e:
    print(f"return value is {e.value}")


###### inject exceptions into a coroutine
print("######" * 12)
coro = f()

try:
    coro.send(None)
    coro.throw(Exception, "blah")
except Exception as e:
    print(f"return value is {e}")



###### Coroutine cancellation with CancelledError
print("######" * 12)
async def f():
    try:
        while True: await asyncio.sleep(0)
    except asyncio.CancelledError as e:
        print("i was canceled")
    else:
        return 111


coro = f()
coro.send(None)
coro.send(None)
try:
    coro.throw(asyncio.CancelledError)
except StopIteration as e:
    # note this is stop iteration
    print(e)

###### Using the event loop to execute coroutines
print("######" * 12)

async def f():
    await asyncio.sleep(0)
    return 222

loop = asyncio.get_event_loop()
coro = f()
result = loop.run_until_complete(coro) # Internally, this is doing all those .send(None) => StopIteration exception => return value 
print(result)