class Animal:
    def eat(self):
        print("Animal can eat")

    def sleep(self):
        print("Animal can Sleep")

# Dog is also a Animal
class Dog(Animal):
    def bark(self):
        print("dog can bark")

dog1=Dog() # Created the Object of DOG [parent class]

dog1.eat() # Calling the parent class Function from child class Object
dog1.sleep() # Calling the parent class Function from child class Object

dog1.bark() # Calling the child class Function from child class Object
