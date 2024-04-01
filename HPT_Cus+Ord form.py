#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from scipy.stats import chi2_contingency

# Load the data from the CSV file
data = pd.read_csv('Costomer+OrderForm.csv')

# Convert the data to a contingency table
contingency_table = pd.crosstab(data['Phillippines'], [data['Indonesia'], data['Malta'], data['India']])

# Perform the chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Set the significance level (alpha)
alpha = 0.05

# Print the results
print(f"Chi-square statistic: {chi2_stat:.4f}")
print(f"p-value: {p_value:.6f}")

# Check if we reject the null hypothesis
if p_value < alpha:
    print("The defective percentages vary significantly among centers.")
else:
    print("The defective percentages do not vary significantly among centers.")


# In[ ]:




