class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"

# Creating an instance of the Student class
student1 = Student("John", 20)

# Printing the student object
print(student1)

# Using str() on the student object
print(str(student1))
