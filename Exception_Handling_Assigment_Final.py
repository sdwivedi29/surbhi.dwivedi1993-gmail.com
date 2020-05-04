#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Task 1:question 1
""""Write a function to compute 5/0 and use try/except to catch the exceptions.
"""""""


# In[1]:


d=int(input("enter any number : "))
def division(d):
    return d/0
try:
    x = d / 0
except ZeroDivisionError:
    print("Division by zero error")
    


# # 2. Implement a Python program to generate all sentences where subject is in
# ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
# ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[2]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in subjects:
    for j in verbs:
        for k in objects:
            h=i+" "+j+" "+k
            print (h,end='.\n')


# In[ ]:




