""" Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.
"""
class Counter:
    count = 0  # Class variable to keep track of object count

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print("=" * 20)
        print("Counter Information:")
        print("=" * 20)
        print("Number of objects created:", cls.count)

# Example usage
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.display_count()
