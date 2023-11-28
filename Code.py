import numpy as np
import matplotlib.pyplot as plt
# Example dataset
original_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
num_resamples = 1000  # You can adjust the number of resamples as needed
#Perform Bootstrapping
resampled_data = np.random.choice(original_data, (num_resamples, len(original_data)), replace=True)
# Example: Calculate the mean of each resampled dataset
resampled_means = np.mean(resampled_data, axis=1)
# Example: Plot the distribution of resampled means
plt.hist(resampled_means, bins=30, edgecolor='black')
plt.title('Distribution of Resampled Means')
plt.xlabel('Mean Value')
plt.ylabel('Frequency')
plt.show()
