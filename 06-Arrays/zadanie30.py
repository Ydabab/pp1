def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example arrays
array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 2, 7, 1, 3, 9, 4, 6, 8]
array3 = [3, 8, 5, 4, 1, 9, 2, 7, 6]

# Sorting and displaying the arrays
print("Original array 1:", array1)
print("Sorted array 1:", bubble_sort(array1))

print("Original array 2:", array2)
print("Sorted array 2:", bubble_sort(array2))

print("Original array 3:", array3)
print("Sorted array 3:", bubble_sort(array3))