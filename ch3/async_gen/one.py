import asyncio

##### Easier with an async generator

class CustomRedis:
    DATABASE = {}
    
    def key_value(self, key:str, value:str|int):
        self.DATABASE.update(
            {key:value}
        )

    async def get(self, key:str) -> str|int|None:
        await asyncio.sleep(1)
        return self.DATABASE.get(key, None)


async def on_at_a_time(redis:CustomRedis, keys:list):
    for k in keys:
        value = await redis.get(k)
        yield value


async def main():
    redis = CustomRedis()
    redis.key_value(key="Americas", value="USA")
    redis.key_value(key="Africa", value="Nigeria")
    redis.key_value(key="Europe", value="England")
    redis.key_value(key="Asia", value="Iran")

    keys = ["Americas", "Africa", "Europe"]


    async for value in on_at_a_time(redis=redis, keys=keys):
        print(value)

asyncio.run(main())