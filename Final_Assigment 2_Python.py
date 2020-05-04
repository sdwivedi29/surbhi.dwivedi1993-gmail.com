#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1: Create the below pattern using nested for loop in Python.

for i in range(0,5):
    for j in range(0,i+1):
         print("*",end=" ")
    print()
for new in range(5,0,-1):
    for new1 in range(new-1,0,-1):
         print("*",end=" ")
    print()  


# In[ ]:





# In[ ]:


2. Write a Python program to reverse a word after accepting the input from the user.

Input word: ineuron
Output: norueni


# In[ ]:


x = input("please enter you string ")

print(x[::-1])

