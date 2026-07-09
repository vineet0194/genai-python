# try:
#     # Code that might raise an exception
# except:
#     # Runs if an exception occurs
# else:
#     # Runs only if NO exception occurs
# finally:
#     # Always runs


def serve_chai(flavor):
    try:
        print(f"preparing {flavor} chai...")
        if (flavor == "unknown"):
            raise ValueError("we don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")

print()

serve_chai("unknown")