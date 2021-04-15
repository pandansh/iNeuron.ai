#!/usr/bin/env python
# coding: utf-8

# # Assignment - 1 (Python Basics) 

# ## Question - 1.

# In[1]:


# Solution 
x = list(range(2000, 3201))
y = []


# In[2]:


for i in x: 
    if (i%7==0) and (i%5==0): 
        y.append((i))
print(y)


# ## Quetsion - 2.

# In[3]:


# Solution 


# In[4]:


first_name = input("Enter you First Name: ")
last_name = input("Enter you Last Name: ")
print("Hi "+ last_name+" "+ first_name)


# ## Question - 3

# In[1]:


# Solution 


# In[3]:


pi = 3.14 
r = 12.00
vol_sphere = 4/3*pi*r**3
print("The volume of the sphere is:", vol_sphere)


# In[ ]:




