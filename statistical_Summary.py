# Descriptive Statistics Summary
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(r'D:\workspace\DataAnalytics\Day2Pandas\tips (1).csv')
# print(data.head())

tip_stats = data['tip'].describe()
print("Descriptive statistics for the tip column : ")
print(tip_stats)

#Additional Statisctics
mean_tip = data['tip'].mean()
median_tip = data['tip'].median()
std_tip = data['tip'].std()
var_tip = data['tip'].var()
skew_tip = data['tip'].skew()
kurtosis_tip = data['tip'].kurtosis()
cv_tip = (std_tip/mean_tip) * 100
q1 = np.percentile(data['tip'], 25)
q2 = np.percentile(data['tip'] , 50)
q3 = np.percentile(data['tip'], 75)

# q1 and _q1 gives same output here
_q1 = data['tip'].quantile(0.25)

print("\n Additional Statisctics for the tip col: ")
print(f"Mean : {mean_tip}")
print(f"Median : {median_tip}")
print(f"Standard Deviation : {std_tip}")
print(f"Variance : {var_tip}")
print(f"Skewness : {skew_tip}")
print(f"Kurtosis : {kurtosis_tip}")
print(f"Coeff of variation : {cv_tip}%")
print(f"Q1 : {q1}")
print(f"Q2 : {q2}")
print(f"Q3 : {q3}")

#plotting the distribution of the tip collumn
plt.figure(figsize=(14, 6))

#Histogram 
plt.subplot(1, 2, 1) # Number of rows , Number of columns , Current subplot number
sns.histplot(data['tip'], bins=20, kde= True)
plt.title("Distribution of tips: ")
plt.xlabel("Tip Amount : ")
plt.ylabel("Frequency : ")

#Bocplot
plt.subplot(1, 2, 2)
sns.boxplot(x = data['tip'])
plt.title('Box Plot of Tips')
plt.xlabel('Tip Amount')

plt.tight_layout()
plt.show()