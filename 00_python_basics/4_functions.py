# Functions

def print_order():
    print("printing")
    pass

def cook_order():
    print("cooking")
    pass

def process():
    print_order()
    cook_order()

# process()

def sum(a, b):
    """
    This is how you write a doc for a func.

    :param a: Takes a number input a
    :param b: Takes a number input b
    :return: (a+b)
    
    """
    # temp = 3          # local
    # global temp       # uses global scope
    # nonlocal temp       # looks for temp in just 1 abstraction above
    temp = 3
    return a+b

temp = 5        # global
# print(sum(a=5, b=6))
print(sum(5, 6))
print(temp)         # will print 3 if u used global keyword

# *args (here named *ingredients) — collects extra positional arguments into a tuple.
# **kwargs (here named **extras) — collects extra keyword arguments into a dictionary.
# Positional argument cannot appear after keyword arguments
                #  *args       **kwargs
def special_chai(*ingredients, **extras):
    print(f"ingredients: {ingredients}")
    print(f"extras: {extras}")

special_chai("cinnamon", "cardamom", sweetner="honey", foam="yes")
            #   tuple                       #   dicts

print("\n\n")

##############################################################################################

# pure function

# does not alter anything => Pure
def pure(num):
    return num*10

total = 0

# does alter something => Impure
def impure(num):
    global total
    total = 3
    return num*10


# lambda function

chai_types = ["light", "kadak", "ginger", "kadak"]
filterOut = list(filter(lambda chai: chai!="kadak", chai_types))  # similar to filter in js
print(filterOut)

print("\n\n")

##############################################################################################

# built in funcs

print(sum.__doc__)
print(sum.__name__)

# help(len)