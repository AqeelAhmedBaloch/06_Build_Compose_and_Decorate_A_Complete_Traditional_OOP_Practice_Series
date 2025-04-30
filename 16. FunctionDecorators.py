"""Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()."""

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("--" * 13)
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("--" * 13)
    print("Hello!")
    print("--" * 13)

# Example usage
say_hello()
