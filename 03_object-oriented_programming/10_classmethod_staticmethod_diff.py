# @classmethod

# A @classmethod is a method that receives the class itself as its first argument (cls), instead of an instance (self).

class ChaiOrder: 
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)

order1 = ChaiOrder.from_dict({
    "tea_type": "masala",
    "sweetness": "medium",
    "size": "large"
})

order2 = ChaiOrder.from_string("ginger-low-medium")

order3 = ChaiOrder("lemon", "low", "small")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)


# python automatically passes cls == ChaiOrder
        # So inside the method:

        # return cls(
        #     order_data["tea_type"],
        #     order_data["sweetness"],
        #     order_data["size"]
        # )

        # becomes:

        # return ChaiOrder(
        #     "masala",
        #     "medium",
        #     "large"
        # )

        # which calls:

        # __init__("masala", "medium", "large")

# ===========================================================================================
#                                @classmethod vs @staticmethod
# ===========================================================================================
#
# | Feature               | @classmethod                    | @staticmethod                |
# |-----------------------|---------------------------------|------------------------------|
# | First Parameter       | cls (class itself)              | None                         |
# | Receives class?       | Yes                             | No                           |
# | Receives instance?    | No                              | No                           |
# | Access class vars?    | Yes (via cls)                   | Only by hardcoding class     |
# | Access instance vars? | No                              | No                           |
# | Create objects?       | Yes (return cls(...))           | Possible, but hardcoded      |
# | Inheritance-friendly? | Yes                             | No                           |
# | Common Use            | Alternative constructors,       | Utility/helper methods       |
# |                       | factory methods                 |                              |
#
# Rule of Thumb:
#
# - Instance Method (self)
#     -> Works with a specific object.
#
# - Class Method (cls)
#     -> Works with the class.
#     -> Often used as an alternative constructor.
#
# - Static Method
#     -> Doesn't need the object or the class.
#     -> Just a utility function grouped inside the class.
#
# ===========================================================================================

# @classmethod:
# Receives the class (cls) as its first argument and is used for operations
# related to the class, such as alternative constructors or modifying class state.

# @staticmethod:
# Receives neither self nor cls and is used for utility/helper functions
# that logically belong to the class but don't depend on its state.