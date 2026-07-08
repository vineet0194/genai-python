# Send args to generators

def chai_customer():
    print("welcome, what chai would you like?")
    order = yield           # yield waits for an ipu
    while True:
        print(f"preparing {order}")
        order = yield

stall = chai_customer()
next(stall)             # start gen

# send(value) is like next(), except it also sends a value into the currently paused yield expression.
stall.send("masala chai")
stall.send("lemon chai")

# send() resumes execution until the next yield (or until the generator ends).
# If there is no next yield, Python keeps running the generator.

print("\n\n\n")

##########################################################################################################

# eg

def myGen():
    name = yield
    while True:
        print(f"your name is {name}")
        name = yield

g = myGen()
next(g)

# g.send("Vineet")        # next with sending values = "Vineet"
# g.send("Ankita")

# yield value → produce data.
# x = yield → consume data.