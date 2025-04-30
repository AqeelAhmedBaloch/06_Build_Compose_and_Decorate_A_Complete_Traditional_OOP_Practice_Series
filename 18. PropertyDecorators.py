"""Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it."""

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price
    print("-" * 22)

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("-" * 22)
        print("Price has been deleted.")
        print("-" * 22)
        del self._price

# Example usage
product = Product("Laptop", 1000)
print(product.price)  # Using the getter

product.price = 1200  # Using the setter
print(product.price)

del product.price  # Using the deleter
