import pandas as pd
import seaborn as sns
import numpy as np
import datetime 
import matplotlib.pyplot as plt

df = pd.read_csv("MS_Dhoni_ODI_record.csv")

print(df.head())

df['opposition'] = df['opposition'].apply(lambda x: x[2:])
df['date'] = pd.to_datetime(df['date'], dayfirst=False)
df['year'] = df['date'].dt.year.astype(int)

df['score'] = df['score'].apply(str)
df['not-out'] = np.where(df['score'].str.endswith('*'), 1, 0)
df_new = df.loc[((df['score'] != 'DNB') & (df['score'] != "TNDB") & (df['runs_scored'] != '-')), 'runs_scored' :]
not_outs = df_new['not-out'].sum()
df_new['runs_scored'] = df_new['runs_scored'].apply(int)
df_new['runs_scored'] = df_new['runs_scored'].astype(int)
total_runs= df_new['runs_scored'].sum()
print(not_outs, total_runs)

print(df_new.shape[0])

print(f'Average : {total_runs/(df_new.shape[0] - not_outs)} ')





# last_match_date = df['date'].dt.date.max().strftime('%B , %')
# number_of_matches = df.shape[0]
# print("Number of matches played : ", number_of_matches)
# # num_of_innings = df.new_shape

# hundreds = (df_new['runs_scored']>=100).sum()
# print("number of hundreds : ",hundreds)

# fifties = ((df_new['runs_scored']>50 ) & (df_new['runs_scored']<100)).sum()
# print("Fifties : ", fifties)

# fours = df_new['fours'].sum()
# print("Number of fours : ", fours)

# sixes = df_new['sixes'].sum()
# print("Number of sixes : ", sixes)

# opposition_count = df['opposition'].value_counts()
# print(opposition_count)

grouped_by_opposition = df_new.groupby('opposition')['runs_scored'].agg(['sum']).reset_index()
print("------------------------------------------------------------------------")
print(grouped_by_opposition)
print("=========================================================================")

# opposition_count.plot(kind="bar", title='number of matches against diff teams : ', figsize=(8,5))
# plt.xlabel(None)
# plt.show()


sns.boxplot(x = 'opposition', y= 'runs_scored', data = df_new)
plt.show()
































