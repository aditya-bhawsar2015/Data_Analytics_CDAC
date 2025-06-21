import matplotlib.pyplot as plt
import numpy as np

a = np.arange(2010,2021)     #years 2010 to 2020
b = np.array([100,120,130,160,180,200,240,260,280,300,320])     #sales data

x = np.arange(20, 70, 5)        #ages between 20 to 65
y = 0.8 *x + 80                 # Blood pressure values

# === Plot 1: Age vs Blood Pressure

plt.figure(figsize=(8,5))
plt.plot(x, y, color = 'green', marker = 'o' , linestyle = '-', label = "BP vs Age")
plt.title("Blood Pressure by age")
plt.xlabel("Age (years)")
plt.ylabel("Blood Pressure (mm Hg )")
plt.grid(True)
plt.legend()
plt.tight_layout()
# plt.show()

# ---------- Year vs Sales ------------
plt.figure(figsize=(8,5))
plt.plot(a,b, color = 'blue', marker = 's', linestyle = '--', label = 'Annual Sales')
plt.title('Annual sales trend')
plt.xlabel('Year')
plt.ylabel('Sales (in $1000s)')
plt.grid(True)
plt.legend()
plt.tight_layout()
# plt.show()

# combined plot
# create a canvas with 1 row and 2 coulmns 
fig, axes = plt.subplots(1, 2 , figsize = (14,5))

# ---------- First Plot (Blood Pressure vs Age) ------------
axes[0].plot(x, y, color='green', marker='o', linestyle='-', label="BP vs Age")
axes[0].set_title("Blood Pressure by Age")
axes[0].set_xlabel("Age (years)")
axes[0].set_ylabel("Blood Pressure (mm Hg)")
axes[0].grid(True)
axes[0].legend()

# ---------- Second Plot (Year vs Sales) ------------
axes[1].plot(a, b, color='blue', marker='s', linestyle='--', label='Annual Sales')
axes[1].set_title('Annual Sales Trend')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Sales (in $1000s)')
axes[1].grid(True)
axes[1].legend()

plt.show()