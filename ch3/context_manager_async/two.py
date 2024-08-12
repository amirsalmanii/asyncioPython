import asyncio
from contextlib import contextmanager, asynccontextmanager
import time

####################################### sync contextmanager
# def download_webpage(url:str):
#     time.sleep(2)
#     return "<h1>hi</h1>"


# def update_stats(url:str):
#     print(f"connect db...")
#     time.sleep(1)
#     print(f"update {url} data in db")


# def process(data):
#     print(f"hey processing {data}")


# @contextmanager
# def web_page(url):
#     data = download_webpage(url)
#     yield data
#     update_stats(url)


# with web_page('google.com') as data:
#     process(data)
####################################### sync


####################################### async asynccontextmanager


async def a_download_webpage(url: str):
    print("dw fn: running to dw...")
    await asyncio.sleep(2)
    print("dw fn: finish dw...")
    return "<h1>hi</h1>"


async def a_update_stats(url: str):
    print(f"update fn: connect db started ...")
    await asyncio.sleep(1)
    print(f"update fn: update {url} data in db")


async def a_process(data):
    print(f"process fn: processing {data} started...")
    await asyncio.sleep(1)
    print(f"process fn: processing {data} finished...")


@asynccontextmanager
async def web_page(url):
    data = await a_download_webpage(url)
    t1 = asyncio.create_task(a_update_stats(url))
    yield data
    await t1


async def a_main():
    async with web_page("google.com") as data:
        await asyncio.create_task(a_process(data))


asyncio.run(a_main())
