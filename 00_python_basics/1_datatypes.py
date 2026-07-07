# Objects

# everything is an object in python
# an object has 3 things: identity, type, value
# id helps use tell if something is mutable or immutable NOT value

# numbers are immutable => value never changes (reference can)
amount = 2                              # amount is a reference that points to the value 2
print(f"1 my amount is: {amount}")

amount = 4                              # this changes the reference of amount, not value
print(f"2 my amount is: {amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 4: {id(4)}")
print(f"ID of amount: {id(amount)}")

print(f"\n\n")

# sets are mutable => value can change, reference stays the same
spice = set()

print(f"intial spice id: {id(spice)}")

spice.add("ginger")
spice.add("cardamom")

print(f"spices: {spice}")
print(f"new spice id: {id(spice)}")

print(f"\n\n")

##################################################################################################################

# Numbers

print(f"test")

a = 14
b = 3

total = a + b
print(f"{total}")

print(f"\n\n")

is_boiling = True

if (is_boiling):
    print("YES")

c = 0
print(f"is c? {bool(c)}")

print(f"\n\n")

##################################################################################################################


# Floats

a = 1.123123123123
b = 2.456456456456

print(f"{b-a}")

print(f"\n\n")

##################################################################################################################

# String

a = "hello there!"

print(a[::2])   #every 2nd (skip i-1)
print(a[2:5])
print(a[1:])
print(a[:3])
print(a[::-1])  #reverse

print(f"\n\n")

labled_text = "Spécial"
encoded_label = labled_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")

print(f"normal label: ", labled_text)
print(f"encoded label: ", encoded_label)
print(f"decoded label: ", decoded_label)

print(f"\n\n")

##################################################################################################################

# Tuples

spices = ("ginger", "cloves", "cinnamon")

(spice1, spice2, spice3) = spices   # tuple unpacking

print(spice1)

a, b = 1, 2     # a = 1, b = 2
print(f"a = {a}, b = {b}")
      
b, a = a, b     # b = a, a = b => a = 2, b = 1
print(f"a = {a}, b = {b}")

if ('ginger' in spices):
    print("YES")

print(f"\n\n")

##################################################################################################################

# List

arr = [1,2,3,4,5]

arr.append(6)
print(arr)

arr.remove(3)
print(arr)

arr.extend([7,8,9])
print(arr)

arr.insert(2, 3)
print(arr)

popped_val = arr.pop()
print(arr)
print("popped =", popped_val)

arr.reverse()
print(arr)

print(max(arr))
print(min(arr))

arr2 = ["temp"] * 3
print(arr2)

arr3 = ["temp", "water"] * 3
print(arr3)

arr4 = bytearray(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(arr4)

arr5 = arr4.replace(b"ABCD", B"ZZZZ")
print(arr5)

print(f"\n\n")

##################################################################################################################

# Sets

setA = {1,2,3}
setB = {3,4,5}

print(setA & setB)  # intersec
print(setA | setB)  # union
print(setA - setB)  # left
print(setB - setA)  # right

frozenset(setA)

if (3 in setA):
    print("PRESENT")

setC = {1,2,3}
frozenset(setC)
setC.add(4)
print(setC)

print(f"\n\n")

##################################################################################################################

# Dictionary

dict1 = {"Ankita": 1, "Vineet": 2, "Vansh": 3}
print(dict1["Ankita"])
print(dict1["Vineet"])

if ("Vineet" in dict1):
    print("Present")

print(dict1.keys())
print(dict1.values())
print(dict1.items())

last_item = dict1.popitem()
print(dict1.items())

note = dict1.get("Vineet", "NOPE, NOTFOUND!")   # key, fallback
print(note)

print(f"\n\n")

##################################################################################################################

import arrow

# Collections
    # imported

# eg for external modules
time = arrow.utcnow()
print(time)

from collections import namedtuple

chai_profile = namedtuple("chai_profile", ["flavor, aroma"])