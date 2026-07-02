# array creation
arr = [1,2,3,4,5]
arr2=[0] * 10
print(arr2)
arr3=list(range(10))
print(arr3)

# Accessing elements  - O(1)
print(arr[0])  # Access first element
print(arr[-1])  # Access last element

# Slicing - O(k) where k is the number of elements in the slice
print(arr[1:4])  # Access elements from index 1 to 3
print(arr[:3])  # Access first three elements
print(arr[2:5])  # Access elements from index 2 to 4
print(arr[::-1])  # Reverse the array

# Modification 
arr[0] = 10  # Modify first element - O(1)
print(arr)  # Print the modified array

arr.append(6)  # Append an element at the end - O(1)
print(arr)  # Print the array after appending

arr.pop()  # Remove the last element - O(1)
print(arr)  # Print the array after popping

arr.insert(2, 15)  # Insert an element at index 2 - O(n)
print(arr)  # Print the array after insertion

arr.pop(2)  # Remove the element at index 2 - O(n)
print(arr)  # Print the array after popping at index 2

# Searching - O(n)
print(3 in arr)  # Check if 3 is in the array
print(arr.index(3))  # Find the index of element 3 - O(n)

#sorting - O(n log n)
arr.sort()  # Sort the array in ascending order
print(arr)  # Print the sorted array
arr.sort(reverse=True)  # Sort the array in descending order
print(arr)  # Print the sorted array in descending order
sorted_arr = sorted(arr)  # Create a new sorted array without modifying the original
print(sorted_arr)  # Print the new sorted array
arr.sort(key=lambda x: x % 2)  # Sort the array based on a custom key (even numbers first)
print(arr)  # Print the array sorted by even numbers first

# 2D Arrays (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)  # Print the 2D array
print(matrix[0][0])  # Access the element at row 0, column 0
print(matrix[1][2])  # Access the element at row 1, column 2

matrix = [[0] * 3 for _ in range(3)]  # Create a 3x3 matrix initialized with zeros
print(matrix)  # Print the 3x3 matrix
matrix =[[0] * 3] * 3  # Create a 3x3 matrix initialized with zeros (not recommended)
print(matrix)  # Print the 3x3 matrix(this creates a shallow copy, so modifying one row will affect all rows)

# length and iteration
print(len(arr))  # Get the length of the array
for i, value in enumerate(arr):  # Iterate through the array with index and value
    print(f"Index: {i}, Value: {value}")
    pass
for i in range(len(arr)):  # Iterate through the array using index
    print(f"Index: {i}, Value: {arr[i]}")
    pass