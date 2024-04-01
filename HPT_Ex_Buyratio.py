#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from scipy.stats import chi2_contingency

# Load the data from the CSV file
data = pd.read_csv('BuyerRatio.csv')

# Convert the strings to numerical values
data = data.replace(['Males', 'Females'], [1, 2])  
data = data.apply(pd.to_numeric, errors='coerce') 

# Convert the data to a contingency table
contingency_table = data.values.T  

# Perform the chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Set the significance level (alpha)
alpha = 0.05

# Print the results
print(f"Chi-square statistic: {chi2_stat:.4f}")
print(f"p-value: {p_value:.6f}")

# Check if we reject the null hypothesis
if p_value < alpha:
    print("The male-female buyer ratios are not similar across regions.")
else:
    print("The male-female buyer ratios are similar across regions.")


# In[ ]:




