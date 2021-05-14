#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
from plotnine import*
import wanrnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


sample = pd.read_csv("Downloads\SampleSuperstore.csv")
sample.head()


# In[5]:


sample.tail()


# In[7]:


sample.shape


# In[8]:


#Checking the type of data


# In[9]:


sample.info()


# In[10]:


#we can see that there is no such value that is empty
sample.describe()


# In[11]:


#Checking if there is duplicate data


# In[13]:


sample.duplicated()


# In[14]:


sample.drop_duplicates()


# In[15]:


sample.nunique()


# In[ ]:





# In[35]:


#correalation between variables. Checking if change in one variable affects the other
sample.corr()


# In[18]:


#Covariance


# In[19]:


sample.cov()


# In[37]:


#Data visualisation
sample.head()


# In[44]:


print(sample['State'].value_counts())
plt.figure(figsize=(15,8))
sns.countplot(x=sample['State'])
plt.xticks(rotation=90)
plt.show()


# In[51]:


plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category', data=sample)
plt.xticks(rotation=90)
plt.show()


# In[52]:





# In[54]:


print(sample['Sub-Category'].value_counts())
plt.figure(figsize=(12,6))
sns.countplot(x=sample['Sub-Category'])
plt.xticks(rotation=90)
plt.show()


# In[55]:


fig,axes = plt.subplots(1,1,figsize=(9,6))
sns.heatmap(sample.corr(), annot= True)
plt.show()


# In[56]:


fig,axes = plt.subplots(1,1,figsize=(9,6))
sns.heatmap(sample.cov(), annot= True)
plt.show()


# In[57]:


sns.countplot(x=sample['Segment'])


# In[58]:


sns.countplot(x=sample['Region'])


# In[61]:


plt.figure(figsize=(40,25))
sns.barplot(x=sample['Sub-Category'], y=sample['Profit'])


# In[62]:


plt.figure(figsize = (10,4))
sns.lineplot('Discount', 'Profit', data = sample, color = 'r', label= 'Discount')
plt.legend()


# In[63]:


sample.hist(bins=50 ,figsize=(20,15))
plt.show()


# In[64]:


figsize=(15,10)
sns.pairplot(sample,hue='Sub-Category')


# In[65]:


grouped=pd.DataFrame(sample.groupby(['Ship Mode','Segment','Category','Sub-Category','State','Region'])['Quantity','Discount','Sales','Profit'].sum().reset_index())
grouped


# In[66]:


sample.groupby("State").Profit.agg(["sum","mean","min","max","count","median","std","var"])


# In[67]:


sns.pairplot(sample)


# In[68]:


fig, axes = plt.subplots(figsize = (10 , 10))

sns.boxplot(sample['Sales'])


# In[69]:


fig, axes = plt.subplots(figsize = (10 , 10))

sns.boxplot(sample['Discount'])


# In[70]:


fig, axes = plt.subplots(figsize = (10 , 10))

sns.boxplot(sample['Profit'])


# In[71]:


fig, ax = plt.subplots(figsize = (10 , 6))
ax.scatter(sample["Sales"] , sample["Profit"])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[ ]:




