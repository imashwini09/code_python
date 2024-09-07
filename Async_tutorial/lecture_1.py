import asyncio
async def hello():
    print("hellopoooo")
    await asyncio.sleep(1)
    print('Hello World!')

async def func1():
    print("func1")
    await asyncio.sleep(2)
    print("hey")

async def main():
    l = await asyncio.gather(hello(),func1())
    print(l)

asyncio.run(main())