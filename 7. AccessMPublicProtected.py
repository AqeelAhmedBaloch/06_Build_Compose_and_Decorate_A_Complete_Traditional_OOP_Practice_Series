"""Create a class Employee with:
a public variable name,
a protected variable _salary, and
a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens."""

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected (by convention)
        self.__ssn = ssn         # Private (name mangled)

# Create an instance
emp = Employee("Aqeel Ahmed", 100000, "0321-2272327")

# Access public variable
print("-" * 20)
print("Name:", emp.name)  # ✅ Accessible

# Access protected variable
print("Salary:", emp._salary)  # ⚠️ Accessible, but should be treated as protected (by convention)
print("-" * 20)

# Access private variable (direct access will fail)
try:
    print("SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError as e:
    print("Error accessing private variable __ssn:", e)

# Access private variable using name mangling
print("SSN (via name mangling):", emp._Employee__ssn)  # ✅ Accessible this way, but not recommended
