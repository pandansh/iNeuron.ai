#!/usr/bin/env python
# coding: utf-8

# In[23]:


# 1. Create Star(*) pattern using nested loop in python


# In[24]:


num_row = int(input("enter the number of rows: "))

for row in range(1, num_row+1):
    for col in range(1, row+1):
        
        print("*", end=" ")
    print()

           
for row in range(num_row+1, 0, -1):
    for col in range(1, row+1):
        
        print("*", end=" ")
    print()


# In[25]:


# 2. Python program to reverse a word after accepting input from user


# In[26]:


a = (input("Enter any word to reverse it: "))

def reverse_fun(s):
    return s[::-1]

print(reverse_fun(a))


# In[ ]:




