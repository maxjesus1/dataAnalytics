#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/niteen11/DataAnalyticsAcademy/master/Python/dataset_diabetes/diabetic_data.csv')


# In[3]:


df.info()


# In[4]:


df.columns


# In[7]:


df.head()


# In[8]:


missing_values


# In[12]:


missing_values


# In[13]:


unique_values


# In[15]:


columns_to_keep=['race','gender','time_in_hospital','number_diagnoses','diabetesMed']


# In[18]:


subset_df=df


# In[19]:


subset_df.head()


# In[20]:


subset_df.head()


# In[21]:


initial_comparison_group=subset_df[subset_df['race']=='AfricanAmerican']


# In[22]:


initial_comparison_group


# In[ ]:




