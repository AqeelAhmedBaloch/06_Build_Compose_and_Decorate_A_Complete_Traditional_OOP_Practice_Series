"""Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it."""

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"ID: {self.emp_id}\nEmployee: {self.name}"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: uses existing Employee object

    def show_department_info(self):
        return f"Department: {self.name}\n{self.employee.get_details()}"

# Example usage
print("Aggregation Example:")
print("-" * 25)
emp = Employee("Ammad", 100)
dept = Department("HR", emp)
print(dept.show_department_info())
print("-" * 25)