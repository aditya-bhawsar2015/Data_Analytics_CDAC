import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'D:\workspace\DataAnalytics\Day4\weight-height.csv')

df_male_height = df[df['Gender'] == 'Male', ['Height']]

print(df_male_height)

