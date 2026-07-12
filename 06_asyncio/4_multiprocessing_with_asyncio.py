import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

# standard way to combine asyncio with process.

# almost the same as using threads with asyncio
# only that you need to declare it all in a __main__

def encrypt(data):
    # time.sleep(3)
    return f"🔒 {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "creditDetails")
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
