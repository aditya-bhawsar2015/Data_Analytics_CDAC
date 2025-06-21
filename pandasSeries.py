import numpy as np
import pandas as pd

# 1. Creating a Series from Python list with default numeric index

myindex = ['USA', 'Canada', 'England']
mydata = [1776, 1867, 1821]

#Series with default integer index
myser = pd.Series(data = mydata)
print("Series with default index :\n", myser)

# 2. Creating a Series with custom index

myser = pd.Series(data = mydata, index=myindex)
print("\n Series with named index :\n ", myser)

# 3. Creating a Series from numpy array

ran_data = np.random.randint(0 , 100 ,4)
print("\n Random data from Numpy array : ", ran_data)
names = ['Alice', 'Bob','Charles', 'Dave']
ages = pd.Series(ran_data, index = names)
print("\n Series from NumPy array : \n", ages)

# 4. Creating a Series from a dictionary

ages_dict ={'Sammy' : 5, 'Frank': 10, 'Spike': 7 }
print("\n Series from Dictionary : \n  ", pd.Series(ages_dict))


# 5. Creating series for imaginary sales data (Q1 and Q2)
q1 = {'Japan' : 80, 'China' : 450, 'India': 200, 'USA': 250}
q2 = {'Brazil' : 100, 'China' : 500, 'India': 210, 'USA': 260}

# Convert Dictionaries into pandas series

sales_Q1 = pd.Series(q1)
sales_Q2 = pd.Series(q2)

# Accessing values by named index
print("\n Sales in Japan for Q1 : ", sales_Q1)

# Integer- based location indexing (default index)
print("\n First entry in Q1 Sales data : ", sales_Q1[0]) 

try:
    print(sales_Q1['France'])  # Non Existing key
    print(sales_Q1['USA  '])   # Extra spaces in key
    print(sales_Q1['usa'])  #Case mismatch
    pass
except KeyError as e:
    print("Error: ", e)

# 7. Series Operation
print("\nSeries keys :", sales_Q1.keys())       #Getting the index(keys)

#broadcasting Operations
print("\n Sales Q1 doubled : \n ", sales_Q1*2)      # Multiplying all sales by 2
print("\n Sales Q2 divided by 100 : \n", sales_Q2 / 100 )

# 8. Handling mismatched indices(NaN Values)

print("\n sales Q1 +sales Q2 (with Nan where no matching key): \n", sales_Q1 + sales_Q2)

#9. handling missing data (Filling Nan with a default value)

print("\n Sales Q1 + Sales Q2 (fill Nan with 0): \n", sales_Q1.add(sales_Q2, fill_value = 0))