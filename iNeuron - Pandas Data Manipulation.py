#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('titanic.csv')
df.head(10)


# In[3]:


df.shape


# In[4]:


df.dtypes


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.describe()


# In[9]:


df.columns


# In[14]:


df[['Name','Sex','Ticket','Embarked']]


# In[16]:


df[['Name','Sex','Ticket','Embarked']].describe()


# In[24]:


df.dtypes[df.dtypes == 'object']


# In[27]:


a = df.dtypes[df.dtypes == 'object'].index


# In[28]:


type(a)


# In[35]:


df[a].describe()


# In[44]:


b=df.dtypes[df.dtypes=='int64']


# In[45]:


b


# In[47]:


b.describe()


# In[48]:


df.columns


# In[51]:


df.Name


# In[54]:


df['Name']


# In[69]:





# In[67]:


df[['Name']]


# In[73]:


df[['Name','SibSp','Survived']][26:56:3]


# In[83]:


sorted(df['Name'])[10:16]


# In[88]:


df['PassengerId'].describe


# In[97]:


a = df[['PassengerId']]


# In[100]:


a


# In[99]:


a1 = df['PassengerId']


# In[101]:


a1


# In[106]:


sorted(df['PassengerId'])


# In[107]:


df.columns


# In[109]:


newp=pd.Categorical(df['Pclass'])


# In[110]:


newp


# In[111]:


df['Cabin']


# In[112]:


import numpy as np 
char_cabin = df['Cabin'].astype(str)


# In[113]:


char_cabin


# In[120]:


[cabin[0] for cabin in char_cabin]


# In[125]:


result = [cabin[0] for cabin in char_cabin]


# In[126]:


df['cabin_1']=result


# In[127]:


df


# In[129]:


df['Age'].isnull().sum()


# In[130]:


df['Age'].isnull()


# In[131]:


df['Age'].isnull()==True


# In[133]:


missing_age = np.where(df['Age'].isnull()==True)


# In[134]:


missing_age


# In[136]:


max(df['Fare'])


# In[141]:


max_fare_index=np.where(df['Fare']==max(df['Fare']))


# In[148]:


df.iloc[max_fare_index][['Name','Age','Fare']]


# In[149]:


# Name, Cabin, with min age 


# In[152]:


min_age_index=np.where(df['Age']==min(df['Age']))


# In[154]:


df.iloc[min_age_index][['Name','Age','Cabin']]


# In[156]:


df['Family'] = df['SibSp'] + df['Parch']


# In[157]:


df['Family'] 


# In[159]:


fam = np.where(df['Family']==max(df['Family']))


# In[160]:


fam


# In[162]:


df.iloc[fam]


# In[163]:


dic = {"q":123, "w":"www", "e":333}
dic


# In[166]:


pd.DataFrame(dic, index=['a','b','c'])


# In[ ]:




