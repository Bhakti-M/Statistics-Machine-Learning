# -*- coding: utf-8 -*-
"""Exercise3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p21VPRkAYYq9WJyrv-NRlaFwaYo4Ls0V
"""

import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset("iris")

"""T-Test (Comparing Petal Lengths of Two Species)"""

from scipy import stats

# Filter data for Setosa and Versicolor species
setosa = iris[iris['species'] == 'setosa']
versicolor = iris[iris['species'] == 'versicolor']

# Perform the t-test
t_stat, p_value = stats.ttest_ind(setosa['petal_length'], versicolor['petal_length'])

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Interpret the results
if p_value < 0.05:
    print("Reject the null hypothesis. The mean petal lengths of Setosa and Versicolor are significantly different.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in mean petal lengths.")

"""Z-Test (Testing Mean Sepal Length of a Species)"""

from statsmodels.stats.weightstats import ztest

# Assuming population standard deviation is known (replace with actual value if known)
pop_std_dev = 0.5

# Filter data for one species (e.g., Setosa)
setosa = iris[iris['species'] == 'setosa']

# Perform the z-test
z_stat, p_value = ztest(setosa['sepal_length'], value=5.0)

print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Interpret the results
if p_value < 0.05:
    print("Reject the null hypothesis. The mean sepal length of Setosa is significantly different from 5.0.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference from 5.0.")

"""ANOVA (Comparing Petal Widths Across All Species)"""

from scipy.stats import f_oneway

# Perform the ANOVA
f_stat, p_value = f_oneway(iris['petal_width'][iris['species'] == 'setosa'],
                          iris['petal_width'][iris['species'] == 'versicolor'],
                          iris['petal_width'][iris['species'] == 'virginica'])

print("F-statistic:", f_stat)
print("P-value:", p_value)

# Interpret the results
if p_value < 0.05:
    print("Reject the null hypothesis. At least one species has a different mean petal width.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in mean petal widths.")

"""Correlation/Regression (Exploring Relationship Between Sepal and Petal Length)


"""

import statsmodels.formula.api as smf

# Perform simple linear regression
model = smf.ols(formula='petal_length ~ sepal_length', data=iris).fit()

# Print the model summary
print(model.summary())

# Calculate Pearson correlation coefficient
corr_coef, p_value = stats.pearsonr(iris['sepal_length'], iris['petal_length'])

print("Pearson correlation coefficient:", corr_coef)
print("P-value:", p_value)

#plot with color-coded species
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=iris)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Relationship Between Sepal and Petal Length")
plt.show()

"""# Explanation

In this exercise, I've performed in the provided exercises, using the Iris dataset . First use an independent t-test to compare the means of the two groups.Afterward To determine if the mean sepal length of one species is significantly different from a specific value (e.g., 5.0).Use a one-sample z-test to compare the sample mean to the hypothesized population mean.And i use a one-way ANOVA to compare the means of multiple groups.To explore the relationship between sepal length and petal length Perform simple linear regression along with a scatter plot.
"""