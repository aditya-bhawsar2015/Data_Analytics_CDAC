import numpy as np
import pandas as pd

# 1. Create a simple DataFrame from existing python list
np.random.seed(101)    # Set seed for reproducibility
mydata = np.random.randint(0 , 101, (4,3))   #Generate random integers in the range [0, 100]
print("Generated Data (mydata) : \n ", mydata)

myindex = ['CA', 'NY', 'AZ','TX']       #CUSTOM ROW INDEX
mycolumns = ['JAN', 'FEB', 'MAR']       #CUSTOM COLUMN NAMES

#create DataFrame without index and columns

df = pd.DataFrame(data = mydata)
print("\n DataFrame without index/colums :\n ", df)

#create DataFrame with custom index

df = pd.DataFrame(data = mydata, index=myindex)
print("\nDataFrame with custom row index : \n ",df)

# create Dataframe with both custom index and cutom clumn names

df = pd.DataFrame(data = mydata, index = myindex, columns=mycolumns)
print("\n DataFrame with custom rows and custom names : \n", df)

# Displaying info about dataframes

print("\n DataFrame Info: ")
print(df.info())

# 2. Create a dataframe from a csv file

df = pd.read_csv('tips (1).csv')
print(df.columns)
print(df.index)
print(df.head(3))
print(df.tail(3))
print(df.info())
print(len(df))
print(df.describe())        # Statistical Summary
print(df.describe().transpose())     # Better Viewing