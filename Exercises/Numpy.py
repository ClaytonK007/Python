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