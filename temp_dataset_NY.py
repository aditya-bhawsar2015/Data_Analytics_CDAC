import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('temp.csv')

# Extract the Ny column only
ny_data = df['NY']

# Calculate Q1 , Q3 and the IQR

Q1 = np.percentile(ny_data, 25)
Q3 = np.percentile(ny_data, 75)
IQR = Q3 - Q1

# Set lower and upper bounds of the outliers

lower_bound = Q1 - (IQR * 1.5)
upper_bound = Q3 + (IQR * 1.5)

# Identify Outlier indices
# True/ False applied to the original dataframe , then .index will give the row numbers for matching condition in the dataframe

outlier_indices = ny_data[(ny_data < lower_bound) | (ny_data > upper_bound)].index
print(outlier_indices)      #Row indices or numbers of outlier records

# Print outlier rows
print("Outlier in NY Tempratures using IQR method : ")
print(df.loc[outlier_indices]) # apply the row numbers to the original Df

# show boxplot for NY Tempratures

plt.figure(figsize=(8,6))
sns.boxplot(y = ny_data, orient='h')
plt.title("NY Tempratures")
plt.show()