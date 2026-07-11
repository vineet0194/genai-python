import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def heavy_func(data):
    print(f"encryption started for {data}")
    time.sleep(3)
    return f"🔒 {data[::-1]}"

async def main(data):
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        results = await loop.run_in_executor(pool, heavy_func, data)
        print(results)

async def ticker():
    for i in range(5):
        print(f"Tick {i}")
        await asyncio.sleep(1)

async def wrapper():
    await asyncio.gather(
        main("vineet"),
        main("ankita"),
        ticker()
    )

if __name__ == "__main__":
    asyncio.run(wrapper())