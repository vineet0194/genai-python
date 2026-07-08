# static methods

# static means "belongs to the class, not to any particular object."

class Utils:
    count = 0       # class variable are by default static (not instance variable)

    @staticmethod
    def clean(text):
        return [item.strip() for item in text.split(',')]
    

str = "water, milk, ginger, honey"

obj = Utils()
# obj.clean(str)

result = Utils.clean(str)
print(result)

Utils.count = 10
print(Utils.count)