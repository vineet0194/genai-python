# Threading example

# Concurrency is the ability of a system to manage multiple tasks that make progress during overlapping time periods.

# Thread - A thread is a unit of execution—a stream of instructions.

import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

# creating threads
# Process
# │
# ├── Thread 1 → take_orders()
# └── Thread 2 → brew_chai()

order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# "Start executing these two functions concurrently."
order_thread.start()
brew_thread.start()

# wait for both to finish

order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")

# import threading
# import time

def func():
    for i in range(4):
        print(i)
        time.sleep(2)

func_thread = threading.Thread(target=func)
func_thread.start()

func_thread.join()

# One Python Process

# ├── Thread 1
# ├── Thread 2
# └── Thread 3

# One GIL
# Shared Memory