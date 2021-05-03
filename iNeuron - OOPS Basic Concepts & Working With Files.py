#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 10


# In[2]:


print(type(i))


# In[3]:


#creating a class


# In[4]:


class test:
    pass


# In[5]:


class person:
    pass


# In[38]:


# Bad practice of creating objects in a class
# In this appraoch it will over right the lates entry as you can see below

p = person
p.name = "Anshul"
p.dob = 12345
p.emp = 1122

a = person
a.name = "John"
a.lastname = "phillips"
a.emp = 4488


# In[39]:


p.name


# In[40]:


p.emp


# In[41]:


a.name


# In[42]:


a.emp


# In[43]:


p.emp


# In[45]:


# Right practive to creat object


# In[108]:


class main_person:
    def __init__(self, name, surname, dob):
        self.name = name
        self.surname = surname
        self.dob = dob 


# In[109]:


p = main_person("Anshul", "Pandey", 26021993)


# In[103]:


s = main_person("Geffery", "jones", 14061990)


# In[110]:


p.name


# In[105]:


s.name1


# In[106]:


p.dob


# In[107]:


s.dob


# In[100]:


s.surname


# In[196]:


class main_person:
    def __init__(self, name, surname, dob):
        self.name = name
        self.surname = surname
        self.dob = dob 
    def test(self,n,m):
        return n+m+self.dob
    # str method is to provide valuable info
    def __str__(self):
        return "%s is a first name and its surname is %s and date of birth is %d" %(self.name, self.surname, self.dob)


# In[197]:


x = main_person("anshul", "pandey", 333333)


# In[198]:


x.name


# In[199]:


x.test(3,4)


# In[200]:


y = main_person("asd","asd",123344)


# In[201]:


y.dob


# In[204]:


x
y


# In[242]:


print(x)
print(y)


# In[245]:


class person:
    def pass_name(self, name):
        self.name = name
        
    def pass_lastname(self, lastname):
        self.lastname = lastname
        
    def pass_dob(self, dob):
        self.dob = dob


# In[248]:


p = person()


# In[249]:


p.pass_lastname("berry")


# In[250]:


p.lastname


# In[251]:


p.pass_name("watson")


# In[252]:


p.name


# In[253]:


p.pass_dob(23154)


# In[254]:


p.dob


# In[258]:


## Abstraction (public, protected and private key)


# In[263]:


# single _ used before variable is protected
    class main_person:
    def __init__(self, name, surname, dob):
        self._name = name
        self._surname = surname
        self._dob = dob 
    def test(self,n,m):
        return n+m+self._dob
    # str method is to provide valuable info
    def __str__(self):
        return "%s is a first name and its surname is %s and date of birth is %d" %(self._name, self.s_urname, self._dob)


# In[264]:


p = main_person("asd","asd",123344)


# In[261]:


p._name


# In[265]:


p.__dict__


# In[268]:


p


# In[280]:


# __ is private variable


# In[295]:


class main_person:
    def __init__(self, name, surname, dob):
        self.__name = name
        self._surname = surname
        self._dob = dob 


# In[296]:


p = main_person("asd","asd",123344)


# In[297]:


p.__dict__


# In[298]:


p.__name


# In[299]:


p._surname


# In[300]:


p._main_person__name


# In[287]:


### ***Inheritence***


# In[303]:


class main_person:
    def __init__(self, name, surname, dob):
        self.name = name
        self.surname = surname
        self.dob = dob 

# ***Inheritence***

class student(main_person):
    def __init__(self,roll_no,college_name, *args):
        super(student, self).__init__(*args)
        self.roll_no = roll_no
        self.college_name = college_name
    
stud = student(56322, "uni", "garry", "malone", 22021990)


# In[304]:


stud.name


# In[306]:


class a:
    def test(self):
        print("Anshul")
        
class b:
    def test(self):
        print("Pandey")
        
#creating an object to inherent from multiple class
        
class c(a,b):
    obja = a()
    objb = b()
    obja.test()
    objb.test()
    
# if you call child class across mutual parent class, it will access the first argument only
  
objc = c()
objc.test()


# In[ ]:




