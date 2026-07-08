# Decorators

# A decorator is a function that takes another function, adds some behavior to it,
# and returns the modified function—without changing the original function's code.

from functools import wraps

def my_decorator(func):

    @wraps(func)                        # do this so that your function metadata doesnt changes
    def wrapper():
        print("before function runs")

        func()

        print("after function runs")
    return wrapper

@my_decorator                       # this is how you pass the function into the decorator
def greet():
    print("hello from decorators")

greet()
# print(greet.__name__)     # returns wrapper => metadata changed
print(greet.__name__)       # if you are using @wraps from functools => metadata not changed