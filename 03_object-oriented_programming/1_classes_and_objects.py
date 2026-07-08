# OOP Intro

class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))       # classes themselves are objects in Python
                        # and the type of every class object is type.

ginger_tea = Chai()

print(type(ginger_tea))

print(type(ginger_tea) is Chai)

print(type(ginger_tea) is ChaiTime)

# In short:
# Chai is an object of type "type".
# ginger_tea is an object of type "Chai".

print("\n\n")

##############################################################################################

