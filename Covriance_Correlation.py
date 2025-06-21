import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\workspace\DataAnalytics\Day4\weight-height.csv')

print(df.head())

# Seprate data based on gender
df_male = df[df['Gender'] ==  'Male']
df_female = df[df['Gender'] ==  'Female']

# calculate correlation
corr_overall = df[['Height', 'Weight']].corr()
corr_male = df_male[['Height', 'Weight']].corr()
corr_female = df_female[['Height', 'Weight']].corr()

print(corr_female)

# calculate covariance

cov_overall = df[['Height','Weight']].cov()
cov_male = df_male[['Height', 'Weight']].cov()
cov_female = df_female[['Height', 'Weight']].cov()

print("Overall Correlation between Height and weight")
print(corr_overall)
print("Male Correlation between Height and weight")
print(corr_male)
print("Female Correlation between Height and weight")
print(corr_female)

print("Overall Covariance between Height and weight")
print(cov_overall)
print("Male Covariance between Height and weight")
print(cov_male)
print("Female Covariance between Height and weight")
print(cov_female)

# Create scatter plots with correlation values
fig, axes = plt.subplots(1, 3 , figsize=(18,6))

# Overall data plot
axes[0].scatter(df['Height'], df['Weight'], color = 'Blue', alpha = 0.5)
axes[0].set_title(f'Overall Correlation: {corr_overall.loc["Height", "Weight"]: .2f}')
axes[0].set_xlabel('Height')
axes[0].set_ylabel('Weight')
axes[0].grid(True)

# Male data plot
axes[1].scatter(df_male['Height'], df_male['Weight'], color = 'Red', alpha = 0.5)
axes[1].set_title(f'Male corration: {corr_male.loc["Height", "Weight"]: .2f}')
axes[1].set_xlabel('Height')
axes[1].set_ylabel('Weight')
axes[1].grid(True)



# Female data plot
axes[2].scatter(df_female['Height'], df_female['Weight'], color = 'green', alpha = 0.5)
axes[2].set_title(f'Male corration: {corr_female.loc["Height", "Weight"]: .2f}')
axes[2].set_xlabel('Height')
axes[2].set_ylabel('Weight')
axes[2].grid(True)


plt.show()