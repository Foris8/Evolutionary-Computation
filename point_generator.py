import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Custom cluster center coordinates
custom_centers = np.array([
    [0.2, 0.4],
    [0.8, 0.8],
    [0.2, 0.8],
    [0.8, 0.2]
])

# Increase the cluster standard deviation to make the centers farther apart
cluster_std = 0.05  # Adjust this value as needed

# Set random seed for reproducibility
np.random.seed(0)

# Define the number of data points
n_samples = 1000

# Generate random data points around custom cluster centers
X, y = make_blobs(n_samples=n_samples, centers=custom_centers, random_state=0, cluster_std=cluster_std)


plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Custom Cluster Center Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
