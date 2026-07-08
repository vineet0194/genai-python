# init

class ChaiOrder:
    # type = None       # redundant
    # size = None
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    
    def summmary(self):
        return f"{self.size}ml of {self.type} chai"
    
order1 = ChaiOrder("Masala", 200)
order2 = ChaiOrder("Ginger", 300)

print(order1.summmary())
print(order2.summmary())