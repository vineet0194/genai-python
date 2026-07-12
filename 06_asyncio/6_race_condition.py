import threading

# A race condition occurs when multiple threads access and modify the same shared data simultaneously,
# and the final result depends on the order in which they execute.
# This is called a race condition because the threads are effectively "racing" to update the shared variable, and the outcome depends on the timing of their execution.

chai_stock = 0

def restock():
    global chai_stock

    for _ in range(100_000):
        chai_stock += 1
    
threads = [threading.Thread(target=restock) for i in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print("Chai Stock: ", chai_stock)