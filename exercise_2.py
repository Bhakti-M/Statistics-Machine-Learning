# -*- coding: utf-8 -*-
"""Exercise_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-Fk2J73vwX33ql3Bn9_vE1Jt53QT4uua
"""

import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

"""Data Loading and Overview :



"""

iris = sns.load_dataset('iris')
print(iris.head())

"""Simple Random Sampling"""

sample = iris.sample(n=30,random_state=42)
print(sample)

# Repeat the random sampling 100 times, calculating the mean sepal length each time
sample_means = []
for _ in range(100):
    sample = iris.sample(n=30)
    sample_mean = sample['sepal_length'].mean()
    sample_means.append(sample_mean)

# Plot the distribution of sample means
plt.hist(sample_means, bins=20, edgecolor='black')
plt.xlabel('Sample Mean Sepal Length')
plt.ylabel('Frequency')
plt.title('Distribution of Sample Means')
plt.show()

"""Implementing Different Sampling Methods:


"""

import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],columns=iris['feature_names'] + ['target'])


# Random Sampling
random_sample = data.sample(n=100)

# Systematic Sampling
step = len(data) // 10
systematic_sample = data.iloc[::step]

# Stratified Sampling
stratified_sample = data.groupby('target', group_keys=False).apply(lambda x: x.sample(min(len(x), 20)))

# Cluster Sampling
# Assuming 'target' represents the clusters
selected_clusters = np.random.choice(data['target'].unique(), 2, replace=False)
cluster_sample = data[data['target'].isin(selected_clusters)]

print("Random Sample:\n", random_sample.head())
print("Systematic Sample:\n", systematic_sample.head())
print("Stratified Sample:\n", stratified_sample.head())
print("Cluster Sample:\n", cluster_sample.head())

"""The Effect of Sample Size and Independence on CLT Assumptions :"""

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                    columns=iris['feature_names'] + ['target'])

feature_to_use = 'sepal length (cm)'

# Define sample sizes
sample_sizes = [10, 30, 50, 100]

# Calculate sample means for each size
sample_means = {size: [] for size in sample_sizes}
for size in sample_sizes:
    for _ in range(1000):
        sample = data.sample(size)
        # Access the column using the correct name
        sample_means[size].append(sample[feature_to_use].mean())

# Plotting the results with enhancements
fig, ax = plt.subplots(figsize=(10, 6))

for size, means in sample_means.items():
    ax.hist(means,
            bins=20,
            alpha=0.7,
            label=f'Sample size {size}',
            edgecolor='black')

ax.set_xlabel(f'Mean {feature_to_use}', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.set_title(
    f'Effect of Sample Size on Distribution of Mean {feature_to_use}',
    fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, linestyle='--', alpha=0.5)

plt.show()

"""Systematic Sampling By Taking 20% of Dataset :"""

def systematic_sampling(df, sample_size):
    interval = len(df) // sample_size
    start = np.random.randint(0, interval)
    indices = np.arange(start, len(df), interval)
    return df.iloc[indices]

# Load the Iris dataset
iris = load_iris()
# Convert the Iris data to a pandas DataFrame
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])

# Rename the 'sepal length (cm)' column to 'sepal_length'
# for consistency with the plotting code
iris_df = iris_df.rename(columns={'sepal length (cm)': 'sepal_length'})


# Calculate the sample size for 20% of the dataset
sample_size = int(len(iris_df) * 0.2)

# Perform systematic sampling
sample_20 = systematic_sampling(iris_df, sample_size)

# Original vs. Systematic Sample
plt.figure(figsize=(8, 6))
sns.kdeplot(iris_df['sepal_length'], color='blue', label='Original Dataset')
sns.kdeplot(sample_20['sepal_length'], color='green', label='Systematic Sample')
plt.xlabel('Sepal Length')
plt.ylabel('Density')
plt.title('Original vs. Systematic Sample')
plt.legend()
plt.show()

"""# Explanation:
Here , First i load Iris dataset using seaborn.load_dataset and display the first few rows to know data.After that randomly selects 30 rows from  dataset in a reproducible manner and then displays the sampled data.For the Sample Mean Distribution Analysis create a list to store the sample means.Iterate 100 times, sampling 30 observations each time, calculating the mean sepal length, and appending it to the list and plot the distribution of these 100 sample means using a histogram.to implement systematic sample define a function systematic_sampling.A KDE plot will compare the distribution of sepal lengths between the original Iris dataset and the systematic sample.


"""
