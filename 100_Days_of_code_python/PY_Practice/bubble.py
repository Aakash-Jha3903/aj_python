print(len("👀"))


# algorithm for bubble sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print ("Sorted array is:", end=" ")
for i in range(len(arr)):
    print("%d" %arr[i], end=" ")
    bubble_sort([64, 34, 25, 12, 22, 11,
                 90])