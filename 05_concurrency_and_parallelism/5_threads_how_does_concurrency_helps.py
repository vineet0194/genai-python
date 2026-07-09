import threading
import time

def boil_milk():
    print(f"Boiling milk...\n")
    time.sleep(1)
    print(f"Milk boiled...\n")

def toast_bun():
    print(f"Toasting bun...\n")
    time.sleep(2)
    print(f"Done with bun toast...\n")

# boil_milk()
# toast_bun()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"total time taken = {end-start:.2f}s")