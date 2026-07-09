# multiple exceptions

def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        if not isinstance(quantity, int):
            raise TypeError
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("not in menu!")
    except TypeError:
        print("Quantity must be a number")
    else:
        print("order processed")
    finally:
        print("NEXT CUSTOMER!")

process_order("elaichi", 2)
print()

process_order("masala", "two")
print()

process_order("masala", 2)
print()