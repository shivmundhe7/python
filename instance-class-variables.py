class Employee:
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 

    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount}")

emp1 = Employee("Shiv")
emp1.raise_amount = 0.3
emp1.showDetails()

emp2 = Employee("Shubham")
emp2.showDetails()