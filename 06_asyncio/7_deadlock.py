import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

# threading.Lock in Python gives you mutual exclusion (often called a mutex).
# It ensures that only one thread at a time can execute a critical section of code.

# When a thread does: "with lock:"
# it:
    # Acquires the lock.
    # Executes the block.
    # Releases the lock automatically when leaving the with block.

# If another thread tries to acquire the same lock while it's already held, it waits.

def task_1():
    with lock_a:
        print("task1 acquired lock_a")
        with lock_b:
            print("task1 acquired lock b")

def task_2():
    with lock_b:
        print("task2 acquired lock_b")
        with lock_a:
            print("taskb acquired lock a")

t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)

t1.start()
t2.start()

t1.join()
t2.join()

# t1 acquires lock_a, at the same time t2 acquires lock_b
# then t1 tries to get lock_b (withheld by t2), at the same time t2 tries to get lock_a (withheld by t1)
# ! this is a DEADLOCK situation

# A deadlock occurs when: Two or more threads are waiting indefinitely for each other to release resources.

# may happen in this code that you do not get a deadlock, that depends on OS scheduler 
# for eg: if it lets t1 run entirely before even starting to run t2 or vice-versa