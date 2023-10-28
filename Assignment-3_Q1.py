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


# In[2]:


cutlets = pd.read_csv('Cutlets.csv')    #Importing Files#
cutlets.head(10)


# In[3]:


cutlets.describe()    #Applying Descriptive Statistics#


# In[4]:


cutlets.isnull().sum()   #Checking for Null Values#


# In[5]:


cutlets[cutlets.duplicated()].shape #Checking for Duplicate Values#


# In[6]:


cutlets[cutlets.duplicated()]


# In[7]:


cutlets.info()    #Checking the data type


# In[8]:


#Plotting the data

plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.boxplot(cutlets['Unit A'])
plt.title('Unit A')
plt.subplot(122)
plt.boxplot(cutlets['Unit B'])
plt.title('Unit B')
plt.show()


# In[9]:


plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.hist(cutlets['Unit A'], bins = 15)
plt.title('Unit A')
plt.subplot(122)
plt.hist(cutlets['Unit B'], bins = 15)
plt.title('Unit B')
plt.show()


# In[10]:


plt.figure(figsize = (8,6))
labels = ['Unit A', 'Unit B']
sns.distplot(cutlets['Unit A'], kde = True)
sns.distplot(cutlets['Unit B'],hist = True)
plt.legend(labels)


# In[11]:


#Plotting Q-Q plot to check whether the distribution follows normal distribution or not

sm.qqplot(cutlets["Unit A"], line = 'q')
plt.title('Unit A')
sm.qqplot(cutlets["Unit B"], line = 'q')
plt.title('Unit B')
plt.show()


# In[15]:


#Compare Evidences with Hypothesis using t-statistics
statistic , p_value = stats.ttest_ind(cutlets['Unit A'],cutlets['Unit B'])
print('p_value=',p_value)


# In[16]:


#Compare p_value with ''(Significane Level)
#If p_value is  '' we failed to reject Null Hypothesis because of lack of evidence
#If p_value is = '' we reject Null Hypothesis
#interpreting p-value

alpha = 0.025
print('Significnace=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
    print('We reject Null Hypothesis there is a significance difference between two Units A and B')
else:
    print('We fail to reject Null hypothesis')

