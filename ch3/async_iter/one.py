import asyncio

##### A traditional, nonasync iterator

# class A:
#     def __init__(self, start_point:int, stop_point:int) -> None:
#         self.stop_point = stop_point
#         self.state = start_point
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.state == self.stop_point:
#             raise StopIteration
#         else:
#             self.state += 1
#             return self.state


# my_custom_iter = A(start_point=0, stop_point=1)
# for i in my_custom_iter:
#     print(i)

##### Async iterator 

class CustomRedis:
    DATABASE = {}
    
    def key_value(self, key:str, value:str|int):
        self.DATABASE.update(
            {key:value}
        )

    async def get(self, key:str) -> str|int|None:
        await asyncio.sleep(1)
        return self.DATABASE.get(key, None)


class B:
    def __init__(self, redis:CustomRedis, keys:list) -> None:
        self.redis = redis
        self.keys = keys
        
    def __aiter__(self):
        self.keys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            key = next(self.keys)
        except StopIteration:
            raise StopAsyncIteration
        else:
            value = await self.redis.get(key)
            return value

async def main():
    redis = CustomRedis()
    redis.key_value(key="Americas", value="USA")
    redis.key_value(key="Africa", value="Nigeria")
    redis.key_value(key="Europe", value="England")
    redis.key_value(key="Asia", value="Iran")

    keys = ["Americas", "Africa", "Europe"]

    async for value in B(redis=redis, keys=keys):
       print(value)


asyncio.run(main())
