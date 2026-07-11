import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# blocking function => blocks the main thread from execution
# If called directly inside an async program, it would block the event loop.
def blocking_func(name):       
    print(f"hi {name}!")
    time.sleep(3)
    return "3 secs are done"

async def main():
    # get me a reference to the currently running event loop.
    loop = asyncio.get_running_loop()

    # similar to pool = ThreadPoolExecutor(), create set of worker threads for me
    # with keyword for context management
    with ThreadPoolExecutor() as pool:
        # i dont want this blocking function to run in my main thread, so what do i do?
        # i delegate this func to one of the worker threads that ThreadPoolExecutor just created for me
        #            in this loop, execute  with pool, with target, with args
        response = await loop.run_in_executor(pool, blocking_func, "vineet")
        print(response)
    

asyncio.run(main())