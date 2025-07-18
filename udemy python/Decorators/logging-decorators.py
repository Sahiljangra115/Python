from functools import wraps
def logging_decoraors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Done calling {func.__name__}")
        return result
    return wrapper

@logging_decoraors
def greet(typer):
    print(f"{typer} I'm done 🎉")

greet("Hello! Everyone 👋")
