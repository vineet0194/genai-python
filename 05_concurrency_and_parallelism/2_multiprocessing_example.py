# Threading example

# Parallelism is the ability of a system to execute multiple tasks at the exact same time.

# Core - A core is an actual processing unit inside your CPU.

import multiprocessing
import time

def brew_chai(name):
    print(f"Start of brew {name}...")
    time.sleep(2)
    print(f"End of brew {name}...")

brew_process = multiprocessing.Process

# Main Process
# ├── Process 1 -> brew_chai("chai maker #1")
# ├── Process 2 -> brew_chai("chai maker #2")
# └── Process 3 -> brew_chai("chai maker #3")

if __name__ == "__main__":
# tells whether the current scrit is being run as main program or being imported as a module
    chai_makers = [
        multiprocessing.Process(target=brew_chai, args=(f"chai maker #{i+1}",))
        for i in range(3)
    ]

    # starting
    for p in chai_makers:
        p.start()
    
    # wait for all to complete
    for p in chai_makers:
        p.join()

# Process 1
# ├── Python Interpreter
# ├── GIL
# └── Memory

# Process 2
# ├── Python Interpreter
# ├── GIL
# └── Memory

# Process 3
# ├── Python Interpreter
# ├── GIL
# └── Memory