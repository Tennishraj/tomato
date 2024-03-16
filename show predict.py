#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
data=pd.read_csv("Movie Interests.csv")
data.head(20)


# In[7]:


input_data=data.drop(columns=["Interest"])
input_data


# In[8]:


output_data=data["Interest"]


# In[9]:


output_data


# In[11]:


from sklearn.tree import DecisionTreeClassifier
data=DecisionTreeClassifier()
data.fit(input_data,output_data)
data.predict([[9,1],[33,0]])


# In[ ]:




