"""Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function."""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Example usage
multiplier = Multiplier(10)

# Test using callable()
print('-' * 22)
print("\t",callable(multiplier))  # Should return True

# Test by calling the object like a function
result = multiplier(10)  # This is equivalent to multiplier.__call__(10)
print('-' * 22)
print("\t",result)  # Should print 50
print('-' * 22)
