# exception handling

chai_menu = {
    "masala": 30,
    "ginger": 40
}

print("code started")

try:
    print(chai_menu["elaichi"])
except KeyError:
    print("key doesnt exist")
finally:
    print("code ended")
