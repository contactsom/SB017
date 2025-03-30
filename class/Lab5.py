class Student:
    def __init__(self): # Default Function which do Initialization
        self.name=""
        self.age = None
        self.salary = 5000

    def getDetails(self):
        print("Hello I am ",self.name)
        print("Hello my Age is  ",self.age)
        print("Hello my Salary is ",self.salary)

student=Student() # Creating the Object of Student


student.getDetails()
