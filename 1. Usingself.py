"""Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
"""
class student:
    def __init__(self, rollno ,name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print("-" * 20)
        print("Student Information: \n")
        print("Roll No:" , self.rollno)
        print("Student Name:" , self.name) 
        print("Marks : " , self.marks)
    
student1 = student(286688,"Aqeel Ahmed Baloch", 90 )
student1.display()
        