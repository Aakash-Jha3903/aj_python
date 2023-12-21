
def factorial():
    n = int(input("Enter the the no. ,to find its factorial : "))
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(f"The factorial of {n} is {fact}")

def recursion_fact():
    n = int(input("Enter the the no. ,to find its factorial : "))

    def fact(n):
        if n < 0:
            print("Please enter a postive number !")
            recursion_fact()
        elif n == 0 or n == 1:
            return 1
        else:
            return n*fact(n-1)

    z = fact(n)
    print(f"The factorial of {n} is {z}")


factorial()
recursion_fact()