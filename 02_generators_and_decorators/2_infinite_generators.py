# Infinite Generator

def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"        # yield returns a value and pauses the generator again.
        count += 1

refill = infinite_chai()

refill2 = infinite_chai()

for _ in range(3):
    print(next(refill))     # 1 2 3         # next resume the gen, run until next yield/generator ends

print()

for _ in range(6):
    print(next(refill2))    # 1 2 3 4 5 6