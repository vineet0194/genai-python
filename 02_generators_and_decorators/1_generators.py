# Generators

# you same memory
# sometimes you don't want the results immediately
# lazy evaluation

# The key difference is that a generator function doesn't execute all at once. Instead, it pauses and resumes its execution every time you ask for the next value.

# generator example
def serve_chai():
    yield "Cup1: Masala Chai"
    yield "Cup2: Ginger Chai"
    yield "Cup3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["cup1", "cup2", "cup3"]

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

# chai = get_chai_list();
# print(chai)

chai = get_chai_gen();      # pointer/reference to the method
print(next(chai))           # prints the first yield value and pauses the method/function
print(next(chai))           # continues from where it is paused
print(next(chai))           # WILL GIVE ERROR