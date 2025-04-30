"""Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class."""

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print("-" * 20)
        print("Car Information:")
        print(f"{self.brand} car has started.")  # Public method

# Instantiate the class
my_car = Car("Toyota Vitz")

# Access public variable
print("Brand:", my_car.brand)

# Access public method
my_car.start()
