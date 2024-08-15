import asyncio
import janus


async def producer(queue):
    for i in range(5):
        print(f'Producing {i}')
        await queue.async_q.put(i)  # Put item into the queue
        await asyncio.sleep(1)  # Simulate some work
    await queue.async_q.put(None)

async def consumer(queue):
    while True:
        item = await queue.async_q.get()  # Get item from the queue
        if item is None:  # Check for termination signal
            break
        print(f'Consuming {item}')
        await asyncio.sleep(2)  # Simulate some work

async def main():
    # Create a Janus queue
    janus_queue = janus.Queue()
    # Create and run producer and consumer tasks
    await asyncio.gather(producer(janus_queue), consumer(janus_queue))
    print('All done!')

asyncio.run(main())