import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_rows", None)
df_2015 = pd.read_csv(r'D:\workspace\DataAnalytics\Day5\marathon_results_2015.csv')
df_2016 = pd.read_csv(r"D:\workspace\DataAnalytics\Day5\marathon_results_2016.csv")
df_2017 = pd.read_csv(r"D:\workspace\DataAnalytics\Day5\marathon_results_2017.csv")

df = pd.concat([df_2015, df_2016, df_2017]).reset_index()
df[['Hours', 'Minutes', 'Seconds']] = df['Official Time'].str.split(":", expand = True).astype(int)
df[['Pace_Hours', 'Pace_Minutes', 'Pace_Seconds']] = df['Pace'].str.split(":", expand = True).astype(int)

df['official_seconds'] = (df['Hours']*3600) + (df['Minutes']*60) + (df['Seconds'])
df['pace_seconds'] = (df['Pace_Hours']*3600) + (df['Pace_Minutes']*60) + df['Pace_Seconds']

time_corr = df[['official_seconds', 'pace_seconds']].corr()
print(time_corr)

sns.scatterplot(df['official_seconds'], df['pace_seconds'], color='red', alpha=0.5)
# sns.heatmap(time_corr)
plt.show()


print(df.head())