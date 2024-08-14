import asyncio


# Refresher for using KeyboardInterrupt as a SIGINT handler

async def main():
    while True:
        print("You App Is Running!!!")
        await asyncio.sleep(1)
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        print("Got Signal: SIGINT, shutting down")
    
    tasks = asyncio.all_tasks(loop=loop)
    for task in tasks:
        task.cancel()
    
    cancels = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(cancels)
    print("all tasks canceled")
    loop.close()