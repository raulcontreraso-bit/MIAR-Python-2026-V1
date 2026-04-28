#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# We use the read_excel function to bring the file into Python
df = pd.read_excel('grades.xlsx')

# This shows us the first few rows to make sure it worked
print("--- Data Loaded Successfully ---")
print(df.head())
# In[ ]:
# In[ ]:




