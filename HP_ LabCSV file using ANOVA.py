#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from scipy.stats import f_oneway

# Load the data from the CSV file
data = pd.read_csv('LabTAT.csv')


# In[3]:


# Perform one-way ANOVA
stat, p_value = f_oneway(data['Laboratory 1'], data['Laboratory 2'], data['Laboratory 3'], data['Laboratory 4'])

# Print the results
print(f'F-statistic: {stat:.4f}')
print(f'p-value: {p_value:.6f}')


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# F-statistic and p-value
F_statistic = 3.9543
p_value = 0.008676

# Define the labels and values for the bar plot
labels = ['F-statistic', 'p-value']
values = [F_statistic, p_value]

# Create a bar plot
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'green'])
plt.title('ANOVA Results')
plt.ylabel('Value')
plt.axhline(y=0.05, color='r', linestyle='--', label='Significance Level (0.05)')
plt.legend()
plt.show()


# In[7]:


import pandas as pd
from scipy.stats import f_oneway

# Load the data from the CSV file
data = pd.read_csv('LabTAT.csv')

# Convert the data frame to a dictionary
lab_data = {
    'Laboratory 1': data['Laboratory 1'].tolist(),
    'Laboratory 2': data['Laboratory 2'].tolist(),
    'Laboratory 3': data['Laboratory 3'].tolist(),
    'Laboratory 4': data['Laboratory 4'].tolist()
}

# Perform one-way ANOVA
stat, p_value = f_oneway(lab_data['Laboratory 1'], lab_data['Laboratory 2'], lab_data['Laboratory 3'], lab_data['Laboratory 4'])

# Print the results
print(f'F-statistic: {stat:.4f}')
print(f'p-value: {p_value:.6f}')


# In[ ]:




