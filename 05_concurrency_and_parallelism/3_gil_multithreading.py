from threading import *
from time import time

# The important point is:

# ! The GIL is not held by one thread until it finishes its entire function.
# ! Instead, CPython periodically releases the GIL and lets another runnable thread acquire it. This is called thread switching.

# Why doesn't Thread 1 keep the GIL forever?

# If it did, one CPU-bound thread could starve every other thread.
# So CPython intentionally switches threads every few milliseconds (or after certain interpreter events) to keep the program responsive.

count = 0       # shared between threads, if u define it in func => local scope
def brew_chai():
    print(f"{current_thread().name} started brewing...")
    for _ in range(100_000_000):
        global count
        # print(f"{current_thread().name} INCREMENTING")
        count += 1
    print(f"{current_thread().name} finished brewing..., new value = {count}")

thread1 = Thread(target=brew_chai, name="Barista-1")
thread2 = Thread(target=brew_chai, name="Barista-2")

start = time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time()

print(f"total time taken = {end-start:.2f} seconds")