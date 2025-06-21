import matplotlib.pyplot as plt
import seaborn as sns

commuter_times = [16, 8, 35, 17, 13, 15, 15, 5, 16, 25, 20, 20, 12, 10, 64]

# create a boxplot to show the outliers

plt.figure(figsize=(10,6))
sns.boxplot(data=commuter_times, orient = 'h')
plt.title("Boxplot of Commuter Times")
plt.xlabel('Minutes')
plt.show()
