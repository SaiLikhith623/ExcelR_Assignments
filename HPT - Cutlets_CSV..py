#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy.stats import shapiro

# Load the data
data = pd.read_csv('Cutlets.csv')

# Perform Shapiro-Wilk test for normality
stat_a, p_a = shapiro(data['Unit A'])
stat_b, p_b = shapiro(data['Unit B'])

# Print the results
print('Unit A - Shapiro-Wilk Statistic:', stat_a, 'p-value:', p_a)
print('Unit B - Shapiro-Wilk Statistic:', stat_b, 'p-value:', p_b)


# In[2]:


from scipy.stats import ttest_ind

# Perform two-sample t-test
t_stat, p_value = ttest_ind(data['Unit A'], data['Unit B'])

# Print the results
print('t-statistic:', t_stat)
print('p-value:', p_value)


# In[5]:


# Define the t-statistic and p-value
t_statistic = 0.7228688704678063
p_value = 0.4722394724599501

# Define the significance level (alpha)
alpha = 0.05

# Check if the p-value is less than the significance level
if p_value < alpha:
    print("Reject the null hypothesis.")  
    print("There is enough evidence to support the alternative hypothesis.")  
else:
    print("Fail to reject the null hypothesis.") 
    print("There is not enough evidence to support the alternative hypothesis.")  

print("t-statistic:", t_statistic)
print("p-value:", p_value)


# In[9]:


import matplotlib.pyplot as plt
from scipy import stats

# Define the t-statistic and p-value
t_statistic = 0.7228688704678063
p_value = 0.4722394724599501
significance_level = 0.05

# Create a plot
plt.figure(figsize=(8, 6))
df = 20  
t_values = np.linspace(-4, 4, 1000)
t_distribution = stats.t.pdf(t_values, df)

plt.plot(t_values, t_distribution, label='t-distribution', color='blue')
plt.fill_between(t_values, 0, t_distribution, where=(abs(t_values) > abs(t_statistic)), color='gray', alpha=0.5, label='p-value region')
plt.axvline(x=t_statistic, color='red', linestyle='--', label='t-statistic')
critical_value = stats.t.ppf(1 - significance_level / 2, df)
plt.axvline(x=critical_value, color='green', linestyle='-.', label='Critical value')

# Add labels and legend
plt.xlabel('t-values')
plt.ylabel('Probability Density')
plt.title('t-Distribution with t-statistic and p-value')
plt.legend()

# Show plot
plt.grid(True)
plt.show()


# In[ ]:




