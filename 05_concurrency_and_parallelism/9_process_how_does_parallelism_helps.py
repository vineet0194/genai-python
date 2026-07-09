import multiprocessing
import time

def cpu_heavy():
    print(f"crunching numbers...")
    total = 0
    for i in range(10**9):
        total += i
    print("DONE")

if __name__ == "__main__":
    start = time.time()

    processes = [multiprocessing.Process(target=cpu_heavy) for _ in range(2)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()

    print(f"total time taken = {end-start:.2f}s")