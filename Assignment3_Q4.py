#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
import statsmodels.api as sm
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from PIL import ImageGrab
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


centers = pd.read_csv('Customer_OrderForm.csv')  #Importing Files#
centers.head(10)


# In[5]:


centers.describe()      #Applying Descriptive Statistics#


# In[6]:


centers.isnull().sum()  #Checking for Null Values#


# In[7]:


centers.info() #Checking the data type#


# In[8]:


print(centers['Phillippines'].value_counts(),'\n',centers['Indonesia'].value_counts(),'\n',centers['Malta'].value_counts(),'\n',centers['India'].value_counts())
#Checking value counts in data#


# In[9]:


#Creating Contingency table#
contingency_table = [[271,267,269,280],
                    [29,33,31,20]]
print(contingency_table)


# In[10]:


#Calculating Expected Values for Observed data#
stat, p, df, exp = stats.chi2_contingency(contingency_table)
print("Statistics = ",stat,"\n",'P_Value = ', p,'\n', 'degree of freedom =', df,'\n', 'Expected Values = ', exp)


# In[11]:


#Defining Expected values and observed values#

observed = np.array([271, 267, 269, 280, 29, 33, 31, 20])
expected = np.array([271.75, 271.75, 271.75, 271.75, 28.25, 28.25, 28.25, 28.25])


# In[12]:


#Compare Evidences with Hypothesis using t-statictic#

test_statistic , p_value = stats.chisquare(observed, expected, ddof = df)
print("Test Statistic = ",test_statistic,'\n', 'p_value =',p_value)


# In[13]:


#Plotting the data#
#Compare p_value with ''(Significane Level) #
#If p_value is ' ' we failed to reject Null Hypothesis because of lack of evidence#
#If p_value is = '' we reject Null Hypothesis #
#interpreting p-value #

alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
    print('We reject Null Hypothesis there is a significance difference between TAT of reports of the laboratories')
else:
    print('We fail to reject Null hypothesis')


# In[ ]:




