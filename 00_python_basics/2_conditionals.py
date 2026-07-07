# Conditionals

cond = True

if (cond):
    print("yes, it is true")

a = int(input("enter a number: "))      #.lower or some other func for string

print("your number:", a)

if (a == 1):
    print("you are number 1")
elif (a == 2):
    print("you are number 2")
else:
    print("you are some other number")

# delivery_fees = (a > 20) ? 0 : 5
# this can be written as:

delivery_fees = 0 if (a>20) else 5

# switch case

match a:
    case 1:
        print("case1")
    case 2:
        print("case2")
    case 3:
        print("case3")
    case _:
        print("outside (1,2,3)")