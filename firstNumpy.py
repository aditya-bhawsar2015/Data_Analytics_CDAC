import numpy as np

# Basic Arrays
list_1 = [1,2,3,4,5,"6"]

arr1 = np.array(list_1)
print(arr1) 

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#1D Array using tuple
arr3 = np.array((7,8,9))
print(arr3)

print("\nBasic Arrays\n", arr1 ,"\n", arr2 ,"\n", arr3)

#Special Arrays

zeroes = np.zeros((2,3))
ones = np.ones((3,2))
identity = np.eye(3) #np.identity(3) can also be used

print("\nSpecial Arrays\n", zeroes ,"\n", ones ,"\n", identity)


empty = np.empty((2,2)) # 2x2 uninitialized array
full = np.full((2,2), 7) # 2x2 array filled with 7
print("\nSpecial Arrays\n", empty ,"\n", full)

#Creating arrays with range
range_array = np.arange(0, 10, 2) # start, stop, step..... 1D array from 0 to 10 with step 2
linspace_array = np.linspace(0, 1, 5) # start, stop, number of samples..... 1D array from 0 to 1 with 5 samples
print("\nCreating arrays with range\n", range_array ,"\n", linspace_array)

#Random arrays
rand = np.random.rand(2,3) # 2x3 array with random values between 0 and 1 2x3 shape
rand_int = np.random.randint(0, 10, (2,2)) # 2x3 array with random integers between 0 and 10

random_numbers=np.random.uniform(0,100,10) # 10 random numbers between 0 and 100
rand_normal = np.random.normal(2,3)   # random numbers from standard normal distribution

rand_custom_number = np.random.normal(5,2, (2,3)) # Normal distribution with mean 5 and std 2, 2x3 shape
print("\nRandom arrays\n", rand ,"\n", rand_int ,"\n", random_numbers ,"\n", rand_normal ,"\n", rand_custom_number)

#String arrays and concatenation
array1 = np.array(['iphone: ', 'price: ']) #Arrays of strings
array2 = np.array(['13', '1000']) #Arrays of strings

#perform element-wise array string concatenation
array3 = np.char.add(array1, array2) #Concatenate two arrays
print(array3)


#reshaping and initializing shapes
reshaped = np.arange(0,12).reshape(3,4) # 1D array of 12 elements reshaped to 3x4
init_like = np.zeros_like(reshaped) # Array of zeros with the same shape as reshaped
print("\nReshaped and initialized shapes\n", reshaped.reshape(4,3) ,"\n", init_like)



# reshaped = np.arange(12).reshape(3,3)    ...... This will give an error because 12 cannot be reshaped into 3x3
# print(reshaped)