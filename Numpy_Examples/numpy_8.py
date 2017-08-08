import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('stockholm_td_adj.dat')

print(np.unique(data[:,1]))

mask_feb = data[:,1] == 2

months = np.arange(1,13)
monthly_mean = [np.mean(data[data[:,1] == month, 3]) for month in months]
fig, ax = plt.subplots()
ax.bar(months, monthly_mean)
ax.set_xlabel("Month")
ax.set_ylabel("Monthly avg. temp.")
plt.show(fig)