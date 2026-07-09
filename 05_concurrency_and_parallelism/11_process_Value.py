from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        # Because this shared object is specifically designed for inter-process sharing, Python gives it an associated lock:
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    # So multiprocessing.Value creates a special piece of memory that is accessible by all processes:
    counter = Value('i', 0)
    processes = [
        Process(target=increment, args=(counter,))
        for _ in range(4)
    ]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print(f"final counter value = {counter.value}")