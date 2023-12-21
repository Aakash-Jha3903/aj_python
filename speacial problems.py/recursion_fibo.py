def recursion_fibo():
    n = int(input("Enter the no. of terms : "))

    def fibo(n):
        if n <= 0:
            print("Please enter a valid positive number !")
            recursion_fibo()
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]  # return to fibo(3) or result
        e = fibo(n-1)
        e.append(e[-1]+e[-2])
        return e
    result = fibo(n)
    print(result)

def without_recursion_fibo_for():
    n = int(input("Enter the no. of terms : "))
    if n <= 0:
        print("Please enter a valid positive number !")
        without_recursion_fibo_for()
    if n == 1:
        print([0])
    else:    
        f = [0, 1]
        for i in range(2, n):
            f.append(f[i-1]+f[i-2])
        print(f)

def without_recursion_fibo_while():
    n = int(input("Enter the no. of terms : "))
    if n <= 0:
        print("Please enter a valid positive number !")
        without_recursion_fibo_while()
    if n == 1:
        print([0])
    else:
        f = [0,1]
        while len(f) < n:
            f.append(f[-1]+f[-2])
        print(f)

recursion_fibo()
without_recursion_fibo_for()
without_recursion_fibo_while()