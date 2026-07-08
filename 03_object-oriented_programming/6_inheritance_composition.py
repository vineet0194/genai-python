# Inheritance

class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} chai...")

# MasalaChai __is a__ BaseChai (inheritance).
class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding cardamom, ginger, cloves")



# ChaiShop __has a__ BaseChai (composition).
class ChaiShop():
    chaiClass = BaseChai        # simply a reference to the class BaseChai

    def __init__(self):
        self.chai = self.chaiClass("Regular")       # creates an instance of BaseChai, and stores

    def serve(self):
        print(f"Serving {self.chai.type} chai")
        self.chai.prepare()

# mixup
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

my_shop = ChaiShop()
fancy = FancyChaiShop()

my_shop.serve() 
fancy.serve()
fancy.chai_cls.add_spices(fancy.chai)

# Composition creates looser coupling.
# Use inheritance when the relationship is genuinely is-a. Use composition when the relationship is has-a or when you want interchangeable parts.

# ! Favor composition over inheritance.