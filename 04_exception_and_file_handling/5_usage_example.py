class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {
        "masala": 20,
        "ginger": 40
    }

    try:
        if (flavor not in menu):
            raise InvalidChaiError("invalid chai!")
        if not isinstance(cups, int):
            raise TypeError("cups must be int")
        total = menu[flavor] * cups
        print(f"your bill for {cups} cups of {flavor} chai = {total}")
    except Exception as e:      # cast all errors
        print(e)
    finally:
        print("thank you for visiting")

bill("mint", 2)
print()

bill("mint", "three")
print()

bill("ginger", 3)
print()