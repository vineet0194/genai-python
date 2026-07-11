import asyncio
import time

# standard way to combine asyncio with threads.

# Execute computations asynchronously using threads or processes.
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)                           # blocking op
    print(f"{item} stock: 42")

async def main():
    # This returns the currently running event loop.
    loop = asyncio.get_running_loop()
    asyncio.get_event_loop

    # pool = ThreadPoolExecutor()       alternative to with

    # "Event loop, give this blocking function to one of the worker threads
    # I will wait asynchronously for the result."   => what run_in_executor does
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())