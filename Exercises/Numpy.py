import numpy as np
#
#   1. Create a 1D NumPy array of numbers from 0 to 9
#
arr = np.arange(10)

print(arr)

#
#   2. Convert 1D array to 2D
# 
arr = np.arange(6)
new_arr = arr.reshape(2,3)

print("Original array:", arr)
print("2D array:\n", new_arr)

#
#   3. Print Array Attributes
#
my_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16)

print("Array shape:", np.shape(my_array))
print("Number of array dimensions:", my_array.ndim)
print("The size of each element in bytes:", my_array.itemsize)

#
#   4. Create a 3×3 NumPy array of all True
#
arr1 = np.full((3, 3), True, dtype=bool)
#   OR
arr2 = np.ones((3, 3), dtype=bool) 

print(arr1)
print(arr2)

#
#   5. Extract the documentation of NumPy’s arange() function
#
np.info(np.arange)

#
#   6. Create a 1D array filled with zeros and another filled with ones
#
arr0 = np.zeros(5)
arr1 = np.ones(5)

print("Zeros", arr0)
print("Ones", arr1)

#
#   7. Create a 1D array of 10 evenly spaced values between 5 and 50
#
arr = np.linspace(5, 50, 10)

print(arr)

#
#   8. Convert a Python list into a NumPy array
#
py_list = [1, 2, 3, 4, 5]
arr_list = np.array(py_list)

print("List converted tpo NumPy array:", arr_list)

#
#   9. Find the memory size of a NumPy array of numbers from 0 to 9
#
arr = np.arange(10)

print("Array:", arr)
print("Memory size in bytes:", arr.nbytes)

#
#   10. Reverse a 1D NumPy array
#
arr = np.arange(10)
reversed_array = arr[::-1]

print("Array:", arr)
print("Reversed_array:", reversed_array)