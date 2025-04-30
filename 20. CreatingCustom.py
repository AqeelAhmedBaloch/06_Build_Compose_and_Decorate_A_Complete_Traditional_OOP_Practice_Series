"""Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except."""

# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        print("-" * 48)
        raise InvalidAgeError(f"Invalid age: {age}. Age must be at least 18.\n")
    else:
        print(f"Age {age} is valid.")
# Example usage with try...except
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Error: {e}")