def print_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# print_info(1, "Hello",'ok', name="Alice", age=25)

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# greet(name="Alice", age=25)

def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    # return 94
    return sum/len(numbers)

x= average(1,2,3,4,5)
# print(x)

def name(**name):
    print(f"Namaste, {name['fname']} {name['mname']}  ! Nice to meet you ")

name(mname="Bihari",lname="Dubey",fname="Krishna")
# name("Bihari","Dubey","Krishna") #error



