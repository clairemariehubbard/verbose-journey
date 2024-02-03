# i want to do a histogram of the data radius_mean variable in breastcancer.csv

import pandas as pd
import matplotlib.pyplot as plt

# read the data
data = pd.read_csv('breastcancer.csv')
# plot the histogram
plt.hist(data['radius_mean'], bins=20, color='blue', edgecolor='black')
plt.title('Histogram of radius_mean')
plt.xlabel('Radius mean')
plt.ylabel('Frequency')
plt.show()

# save the plot
plt.savefig('radius_mean_histogram.png')

