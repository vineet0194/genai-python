import threading

count = 0
lock = threading.Lock()

# The GIL prevents multiple threads from executing Python bytecode at the exact same instant, but it doesn't guarantee that a sequence of bytecode instructions behaves as one indivisible operation. That's why you still need a Lock to protect shared mutable state.

# In short:
# Without a lock: multiple threads can read and update count concurrently, causing lost updates.
# With a lock: only one thread at a time can update count, so every increment is preserved.

def increment():
    global count
    for _ in range(10000):
        with lock:          # locks the mutex => execute atomically
            # The code inside a lock behaves as an atomic critical section with respect to other threads using the same lock.
            print(f"thread {threading.current_thread().name} changed the val")
            count += 1

threads = [threading.Thread(target=increment, name=f"{i}") for i in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"final value = {count}")