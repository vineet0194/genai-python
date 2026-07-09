# file handling

# classic way
try:
    file = open("./order.txt", "w")
    file.write("Masala chai - 2 cups")
finally:
    file.close()

# with keyword, manages closing, exceptions etc.
with open("order.txt", "w") as file:
    file.write("Masala chai - 3 cups")