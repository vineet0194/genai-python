# Logging Decorator

from functools import wraps

def log_activity(func):
    @wraps(func)            #@wraps preserves the metadata of the original function when you decorate it.

    def wrapper(*args, **kwargs):                   # wrapper takes in whatever args func was psd with
        print(f"🚀 Calling : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished : {func.__name__}")
        return result
    
    return wrapper

@log_activity                           # decorator is defined while declaring a function to be decorated
def brew_chai(type):
    print(f"Brewing {type} chai")

# def brew_chai_2(type):                      # this wont be decorated
    # print(f"Brewing {type} chai")

brew_chai("Masala")


# ! control flow: !
# Python reads file
#         │
#         ▼
# Creates original brew_chai
#         │
#         ▼
# Calls log_activity(original_brew_chai)
#         │
#         ▼
# Creates wrapper()
#         │
#         ▼
# Returns wrapper
#         │
#         ▼
# brew_chai now points to wrapper
#         │
# ────────────────────────────────────────────
#         │
# brew_chai("Masala")
#         │
#         ▼
# wrapper("Masala")
#         │
#         ▼
# Print "🚀 Calling..."
#         │
#         ▼
# Call original brew_chai("Masala")
#         │
#         ▼
# Print "Brewing Masala chai"
#         │
#         ▼
# Return to wrapper
#         │
#         ▼
# Print "✅ Finished..."
#         │
#         ▼
# Return None