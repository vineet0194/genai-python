# Auth Decorator

from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if (user_role != "admin"):
            print("Acess denied!")
            # return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access granted")

access_tea_inventory("user")
access_tea_inventory("admin")


# ! control flow: !
# access_tea_inventory("user")
#         │
#         ▼
# wrapper("user")
#         │
#         ▼
# Is user admin?
#         │
#       No │
#         ▼
# Print "Access denied!"
#         │
#         ▼
# STOP
# access_tea_inventory("admin")
#         │
#         ▼
# wrapper("admin")
#         │
#         ▼
# Is user admin?
#         │
#      Yes │
#         ▼
# Call original function
#         │
#         ▼
# Print "Access granted"