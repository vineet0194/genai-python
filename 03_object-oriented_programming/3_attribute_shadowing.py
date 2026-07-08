# Attribute Shadowing

# attributes => An attribute is simply a variable associated with a class or an object.

# An instance attribute with the same name as a class attribute takes precedence during attribute lookup, effectively hiding the class attribute for that instance.

class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()

print("before changing", cutting.temperature)

cutting.temperature = "mild"
print("after changing", cutting.temperature)

print("in the class", Chai.temperature)

del cutting.temperature
print(cutting.temperature)  # gets defaulted to the class's attribute

cutting.cup = "small"
del (cutting.cup)
# print(cutting.cup)        # will result in error as there is no fallback