#11-Jan-26: Statistical Fundamentals for AIML
# This module contains functions for basic statistical operations
# such as mean, median, mode, variance, standard deviation, etc.

# Player A
import numpy as np
scores_A = np.array([10, 20, 30, 40, 50])
freq_A = np.bincount(scores_A)
std_A = np.std(scores_A)
var_A = np.var(scores_A)
mean_A = np.mean(scores_A)
median_A = np.median(scores_A)
print("Player A Scores:", scores_A)
print("Mean of Player A Scores:", mean_A)
print("Median of Player A Scores:", median_A)
print("Standard Deviation of Player A Scores:", std_A)
print("Variance of Player A Scores:", var_A)


# Percentile and Quartiles
percentile_25_A = np.percentile(scores_A, 25)
percentile_50_A = np.percentile(scores_A, 50)
percentile_75_A = np.percentile(scores_A, 75)
print("25th Percentile of Player A Scores:", percentile_25_A)
print("50th Percentile of Player A Scores:", percentile_50_A)
print("75th Percentile of Player A Scores:", percentile_75_A)

import numpy as np
import statsmodels.api as sm
from sm.stats.stattools import medcouple
from sm.stats.stattools import robust_skewness
x = np.array([10, 20, 30, 40, 50])
sk = robust_skewness(x)
print("\nRobust Skewness of x:", sk)
mc = medcouple(x)
print("Medcouple of x:", mc)


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binomial
n, p = 10, 0.5
binom_dist = binomial(n, p)
x = np.arange(0, n+1)
print (x)
pmf = binom.pmf(x, n, p)
print(pmf)
plt.bar(x, pmf)
plt.title('Binomial Distribution PMF (n=10, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.show()
