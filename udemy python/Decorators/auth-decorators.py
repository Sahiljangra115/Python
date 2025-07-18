from functools import wraps

def auth_decorator(func):
    @wraps (func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied. You must be an admin to perform this action.")
            return None
        else:
            return func(user_role)
    return wrapper

@auth_decorator
def detect_access(user_role):
    print(f"User role {user_role} detected successfully. Access granted!")
detect_access("admin")  
# detect_access("guest") 
# detect_access("user")  