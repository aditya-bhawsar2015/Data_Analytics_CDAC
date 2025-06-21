# Arithmetic Operations
import numpy as np


arr = np.arange(0,10)

# Basic Arithmetic Operations


print("Addition (arr+arr) : ",arr + arr)
print("Subtraction (arr-arr) : ",arr - arr)
print("Multiplication (arr*arr) : ",arr * arr)
# Divion (handling divisiion by zero)
print("Division (arr/arr) : ",arr / arr) # divison by zero will give nan


#Exponentiation
print("Cube (arr ** 3) : ", arr ** 3) 



#Universal Functions
print("Square root of arr :", np.sqrt(arr))
print("Exponential (e^arr): ", np.exp(arr))
print("Sine of arr : ", np.sin(arr))
print("Natural log of arr : ", np.log(arr)) # log(0) will give -inf


#Summary Statistics

print("Sum of elements : ", arr.sum())
print("Mean of elements :", arr.mean())
print("Maximum Value : ", arr.max())
print("Minimum Value : ", arr.min())
print("Variance : ", arr.var())
print("Standard Deviation : ", arr.std())



#Reversing an array
arr = np.array([1,2,3,4,5,6,7,8])
reversed_array = arr[::-1]
print("Reversed array :", reversed_array)



#Sorting an array
arr = np.array([5,2,9,1,5,6])
sorted_array = np.sort(arr) 
print("Sorted array :", sorted_array)