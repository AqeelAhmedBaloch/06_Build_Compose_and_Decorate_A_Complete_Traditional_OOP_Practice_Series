"""Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor."""

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example usage
print("--"*12)
teacher = Teacher("Muhammad Bilal", "Python")
print(f"Name: {teacher.name}")
print(f"Subject: {teacher.subject}")
print("--"*12)
