class Student:
    def __init__(self): # Default Function which do Initialization
        self.name="Vivek"
        self.age = 22
        self.salary = 5000

    def getDetails(self):
        print("Hello I am ",self.name)
        print("Hello my Age is  ",self.age)
        print("Hello my Salary is ",self.salary)

student=Student() # Creating the Object of Student


student.getDetails()

'''
this is something like that if we don't specify any argument during calling the 
function then default will come?
'''