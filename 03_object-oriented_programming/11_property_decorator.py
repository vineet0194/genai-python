# @property decorator

class TeaLeaf:
    def __init__(self, age):
        self._age = age             # _ is a naming convention to identify private vars

    @property       # converts this method into a property, without this-> leaf.age() , with-> leaf.age
    def age(self):              # getter
        return self._age

    @age.setter
    def age(self, age):         # setter
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("invalid age")     # raise error if out of bounds
    
leaf = TeaLeaf(2)
print(leaf.age)         # same as leaf.age if you dont use the @property

leaf.age = 4        # instead of directly settings leaf.age = 4, go to setter func and do it with 4
                    # same as leaf.age(4) if you dont use the @property
print(leaf.age) 