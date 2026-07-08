# Namespaces

# In OOP, a namespace is the place where an object's or class's attributes and methods are stored.

class Chai:
    origin = "India"

# Python objects are dynamic. You can add new attributes to classes and instances at runtime:
Chai.is_hot = True      # adding a new class variable
print(Chai.is_hot)

# creating objects

masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False
masala.flavor = "Masala"            # adding a new instance variable (not class)

print(f"Class {Chai.is_hot}")
print(f"Masala {masala.is_hot}")

print(f"Class {Chai.flavor}")       # gives error
print(f"Masala {masala.flavor}")