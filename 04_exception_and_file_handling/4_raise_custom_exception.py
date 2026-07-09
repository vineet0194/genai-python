# custom exceptions

# syntax to create custom exception (u can add other props etc.)
class UnknownFlavourError(Exception):
    pass

def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise UnknownFlavourError("unknown flavor...")
    print(f"brewing {flavor} chai...")

brew_chai("mint")

#     brew_chai("mint")
#     ~~~~~~~~~^^^^^^^^
#   File "c:\Users\Vineet\Documents\Workspace\Code\genai-python\04_error_and_file_handling\4_raise_custom_exception.py", line 9, in brew_chai
#     raise UnknownFlavourError("unknown flavor...")
# UnknownFlavourError: unknown flavor...