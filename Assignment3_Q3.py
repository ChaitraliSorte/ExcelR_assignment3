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


# In[3]:


buyer = pd.read_csv('BuyerRatio.csv')  #Importing Files#
buyer


# In[4]:



table = [[50,142,131,70],
        [435,1523,1356,750]]


# In[7]:


#Applying Chi-Square contingency table to convert observed value into expected value

stats.chi2_contingency(table) 


# In[8]:


observed = np.array([50, 142, 131, 70, 435, 1523, 1356, 750])
expected = np.array([42.76531299,  146.81287862,  131.11756787, 72.30424052, 442.23468701, 1518.18712138, 1355.88243213, 747.69575948])


# In[9]:


#Comparing Evidence with Hypothesis
statistics, p_value = stats.chisquare(observed, expected, ddof = 3)
print("Statistics = ",statistics,"\n",'P_Value = ', p_value)


# In[10]:


#Compare p_value with ''(Significane Level)
#If p_value is '' we failed to reject Null Hypothesis because of lack of evidence
#If p_value is = '' we reject Null Hypothesis
#interpreting p-value

alpha = 0.05
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
    print('We reject Null Hypothesis there is a significance difference between TAT of reports of the laboratories')
else:
    print('We fail to reject Null hypothesis')


# In[ ]:




