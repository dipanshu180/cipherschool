from scipy import stats

# Sample data
group1 = [2, 3, 5, 6, 9]
group2 = [1, 4, 6, 8, 10]

# T-test
t_stat, p_val = stats.ttest_ind(group1, group2)
print("T-statistic:", t_stat)
print("P-value:", p_val)

# Decision
alpha = 0.05
if p_val < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
    
    
from scipy import stats

# Sample data
group1 = [2, 3, 5, 6, 9]
group2 = [1, 4, 6, 8, 10]
group3 = [2, 4, 6, 8, 10]

# ANOVA
f_stat, p_val = stats.f_oneway(group1, group2, group3)
print("F-statistic:", f_stat)
print("P-value:", p_val)

# Decision
alpha = 0.05
if p_val < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
    
    
from scipy import stats
import numpy as np

# Sample data
sample = [2, 3, 5, 6, 9, 1, 4, 6, 8, 10]

# Confidence Interval for the mean
confidence_level = 0.95
degrees_freedom = len(sample) - 1
sample_mean = np.mean(sample)
sample_standard_error = stats.sem(sample)
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)

print("Confidence Interval:", confidence_interval)