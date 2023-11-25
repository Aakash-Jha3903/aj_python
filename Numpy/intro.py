import numpy as np 
print(np.__version__)
 
arr0 = np.array(7)
arr1 = np.array([2,4,6,8])
arr2 = np.array([[1,2,3],[4,5,6]])

arr3 = np.array([[1,2,3],[4,5,6]])
# arr = np.array([2,4,6,8,100] , np.int8)

# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using ""passed tuple:\n", arr) 

print(arr0.dtype)
print(arr1)
print(arr2)
print(arr3.dtype)