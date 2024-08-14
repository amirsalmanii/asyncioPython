"""
in my view and useful case
"""


import asyncio
from time import perf_counter


async def get_http_result() -> str:
    print("-------------------------------> another task is executed")
    await asyncio.sleep(3)
    return "hello world"


class CustomRedis:
    DATABASE = {}

    def key_value(self, key: str, value: str) -> None:
        self.DATABASE.update({key: value})

    async def get(self, key: str) -> str | None:
        print("trying to get the key:", key)
        await asyncio.sleep(1)
        return self.DATABASE.get(key, None)


class B:
    def __init__(self, redis: CustomRedis, keys: list[str]) -> None:
        self.redis = redis
        self.keys = iter(keys)

    def __aiter__(self):
        return self

    async def __anext__(self):
        print("__anext__ called")
        try:
            key = next(self.keys)
        except StopIteration as e:
            raise StopAsyncIteration from e
        else:
            return await self.redis.get(key)


async def main():
    another_task = asyncio.create_task(get_http_result())

    redis = CustomRedis()
    redis.key_value(key="Americas", value="USA")
    redis.key_value(key="Africa", value="Nigeria")
    redis.key_value(key="Europe", value="England")
    redis.key_value(key="Asia", value="Iran")

    keys = ["Americas", "Africa", "Europe"]

    t1 = perf_counter()
    async for value in B(redis=redis, keys=keys):
        print(value)
    print("------------------------------->", await another_task)
    t2 = perf_counter()
    print(f"took {t2 - t1} seconds")


asyncio.run(main())
