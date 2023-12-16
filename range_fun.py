l=[i for i in range(11)]

n= list(range(1, 6))

t= tuple(range(1, 6))
s= str(range(1, 6))
t2 = tuple(i for i in range(11))

print("List: ",l)
print("Tuple: ", t)
print("String: ", s)
print("Generated Tuple t2: ", t2)
print(n)

print(3 in range(5))  # True
print(7 not in range(5))  # True


