# Function Argument
# 1.Default argument
# Keyword argument
# Variable length argument
# Required argument

# # # Required Argument
def average(a=9 , b=1):
    print("Average is", ((a+b)/2))
average (9 ,1)


# # # Default Argument
def name(fname, mname = "Shiv", lname = "mundhe"):
    print("Hello", fname, mname, lname)
name("Shiv", "Shiv")


# # # Keyword Argument (Order Doesnt Matter)
def name(fname, mname = "Shiv", lname = "mundhe"):
    print("Hello", fname, mname, lname)
name("Shiv", "Shiv")


# Variable length argument
def average(*numbers):
    sum = 0 
    for i in numbers:
        sum = sum + i
    print("Average is :", sum / len(numbers))
average(5 , 6)