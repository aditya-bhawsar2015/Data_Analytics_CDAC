# Install pandas if not already installed

import pandas as pd
import numpy as np

team1_df = pd.DataFrame({'Team':['RCB', 'CSK', 'MI', 'SRH', 'LSG'], 'Points' : [1,10,2,3,4]})
team2_df = pd.DataFrame({'Team':['GT', 'PBKS', "DC", 'RR', 'RCB'], 'Points' : [5,6,7,8,9]})

team_df = team1_df + team2_df
new_team_df= pd.concat([team1_df, team2_df])

print(team_df)
print(new_team_df)

df = pd.DataFrame([[1, 2, 3],[4, 5, 6],[7, 8, 9],[np.nan, np.nan, np.nan]], columns=['A', 'B', 'C'])
print(df)

print(df.agg(['sum','min','max']))
print(df.agg(['sum','min','max'], axis=1))