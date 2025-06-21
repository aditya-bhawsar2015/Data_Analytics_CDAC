import numpy as np

#Creating a sample array
arr = np.arange(0,11)
print("Initial Array : ", arr)

#Bracket indexing and selection 
#Get a value at an index
print("Value at index 8 : ", arr[8])

#Get values in a range
print("Values in range [1:5] :" , arr[1:5])
print("Values in range [0:5] : ", arr[0:5])

#Setting values with index range
arr[0:5] = 100
print("After broadcasting [0:5] with 100 : ", arr)

#Reset Array
arr = np.arange(0,11)
print("Reset Array : ", arr)

#impotant notes on slices

slice_of_arr = arr[0:6] # Slice of the array
print("Slice of Array : ", slice_of_arr)

# change slice

slice_of_arr[:] = 99 # Change all values in the slice to 99
print("After modifying slice : ", slice_of_arr)
print("Original Array after modifying slice : ", arr)

# To get a copy 
arr_copy = arr.copy() # Create a copy of the array
print("Copy of Array : ", arr_copy)

#2D Arrays
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print("2D Array : ", arr_2d)

#Indexing row
print("Second row of 2d array : ", arr_2d[1])

#Getting individual element value

print("Element at row 1 and column 2 : ", arr_2d[1][2])


#selecting an array

arr = np.arange(1,11)
print("Array for conditional selection : ", arr)

#Check condition
print("Condition arr>4 :", arr>4)

#store boolean results in another array
bool_arr = arr > 4
print("Boolaean array for >4 :", bool_arr)

# select elements where condition is true
print("Elements where arr>4 :", arr[bool_arr])

# Using condition directly in selection
print("Elements where arr>2 :", arr[arr>2])