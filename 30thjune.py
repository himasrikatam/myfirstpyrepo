import numpy as np
from scipy import stats
data = [10, 20, 30, 40, 50, 60, 70]
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
print("Q1 (25th percentile):", Q1)
print("Q3 (75th percentile):", Q3)
print("IQR:", IQR)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("Lower bound for outliers:", lower_bound)
print("Upper bound for outliers:", upper_bound)
import matplotlib.pyplot as plt
data = [10, 12, 13, 15, 18, 19, 20, 21, 21, 22, 100]
print('mean: ', np.mean(data))
print('median: ', np.median(data))
print('mean: ', stats.mode(data))
variance = np.var(data, ddof=1)
std_dev = np.std(data, ddof=1)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
mad = np.mean(np.abs(data - np.mean(data)))
print("Mean Absolute Deviation:", mad)
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
# whisker is nothing but bounds/range anything outside this are outliers
lower_whisker = Q1 - 1.5 * IQR
upper_whisker = Q3 + 1.5 * IQR
outliers = [x for x in data if x < lower_whisker or x > upper_whisker]
print("Outliers:", outliers)
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title("Box Plot Example")
plt.xlabel("Values")
plt.grid(True)
# plt.show()
# correlation: measure of strenght and directiuon of 2 variables -1 to +1
x=[1,2,3,4,5,6,7]
y=[20,40,20,30,40,80,90]
print("correlation: ", np.corrcoef(x,y)[0,1])
# covariance: measure of direction. directly propositional, +/-
print("Covariance: ",np.cov(x,y,ddof=1)[0,1])
# causation: one variable causes chnage to other.
