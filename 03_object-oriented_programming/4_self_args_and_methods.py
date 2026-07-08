# self, methods

# same as this in cpp

class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    
# describe is an instance method, which means it expects an instance as its first parameter (self).
    
cup = Chaicup()
print(cup.describe())       # gets converted to Chaicup.describe(cup)

# print(Chaicup.describe())     # errors out, until you give the context
# print(Chaicup.describe(cup))  # works the same (you just manually passed the context)