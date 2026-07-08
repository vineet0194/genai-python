# Yield From

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()         # first yield from local chai
    yield from imported_chai()      # then yield from imported chai

# for chai in full_menu():          # first completes all yields from local chai
#     print(chai)                   # then yields all from imported chai

def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
            print(f"preparing {order}")
    except:
        print("stall closed, no more chai")

stall = chai_stall()

print(next(stall))
stall.send("masala chai")

stall.close()   # cleanup