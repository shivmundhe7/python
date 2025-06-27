# dir method in Python 
x = [1, 2, 3]
print(dir(x))

# __dict__  method in Python 
class Person:
    def __init__(self, name, age):
        selfname = name
        self.age = age
p = Person("John ",10)
print(p.__dict__)