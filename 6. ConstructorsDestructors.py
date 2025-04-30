"""Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor)."""

class Logger:
    def __init__(self):
        print("-" * 32)
        print("Logger created.")
        print("-" * 32)
        print("Logger object has been created.")

    def __del__(self):
        print("-" * 32)
        print("Logger destroyed.")
        print("-" * 32)
        print("Logger object has been destroyed.")

# Example usage
log = Logger()

# Manually delete the object (optional, for demonstration)
del log