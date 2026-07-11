import asyncio
import time

# Event Loop - the engine that runs and schedules co-routines
# it continuously checks whether the call stack is empty and whether there are pending tasks in the callback queue or microtask queue.
# one thread + one event loop + multiple coroutines.

# blocking operations => synchronous operations
# non-blocking operations => asynchronous operations

# defining a co-routine
async def brew_chai(name):
    print(f"Brewing {name}...")
    
    await asyncio.sleep(3)
    # time.sleep(3)

    print(f"{name} is ready...")

async def main():
    # similar to Promise.all(...)
    await asyncio.gather(               # gather() schedules all coroutines concurrently.
        brew_chai("Masala Chai"),
        brew_chai("Green Chai"),
        brew_chai("Ginger Chai")
    )

# !running a co-routine, also creates and starts the event loop
# asyncio.run(brew_chai())

# running multiple co-routines  (wrapped under 1 co-routine that "gathers" all others)
asyncio.run(main())

#######################################################################################################

# Whenever you're writing async code, ask:

# Can I await this function?

# ✅ Yes → just await it.
# ❌ No, but it's mostly waiting (disk, blocking I/O, old library) → run_in_executor(ThreadPoolExecutor).
# ❌ No, and it's heavy CPU work → ProcessPoolExecutor or multiprocessing.