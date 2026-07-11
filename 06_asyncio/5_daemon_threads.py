# A daemon thread in Python is a background thread that automatically stops when the main program finishes. Used for non-critical background tasks (eg: logging, monitoring, health check etc. => do so till my main thread is alive)

import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temp...")
        time.sleep(2)
    
    # when my main thread finishes => daemon threads die too
    # alive until the main thread dies
t = threading.Thread(target=monitor_tea_temp, daemon=True)

    # if daemon=False, non-main threads continue to work until logic is finished
    # this is the default nature, treat every new thread as a regular thread
    # alive until it finishes its execution.
# t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")