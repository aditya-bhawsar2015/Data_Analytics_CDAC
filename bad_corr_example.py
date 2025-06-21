import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\workspace\DataAnalytics\Day5\euro.csv')
df = df.dropna()

df['INR'] = df['INR'].astype(float)
df['USD'] = df['USD'].astype(float)
df['CHU'] = df['CHU'].astype(float)

correlation_coeffecient = df['INR'].corr(df['CHU'])
print(f'Correlation Coffecient : {correlation_coeffecient}')

plt.scatter(df['INR'], df['USD'])
plt.xlabel(" Indian Rupees ")
plt.ylabel("US Dollar ")
plt.title(f"Scatter Plot (Correlation : {correlation_coeffecient: .2f})")
plt.legend()
plt.show()
