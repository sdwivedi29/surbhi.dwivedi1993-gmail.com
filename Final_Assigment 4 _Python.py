#!/usr/bin/env python
# coding: utf-8

# # 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[ ]:


class Area:
   def __init__(self,a,b,c):
        self.a=input('please enter length ')
        self.b=input('please enter breadth ')
        self.c=input('Please enter height ')

f=Area(a,b,c)
f.area()

class Sub(Area):
    area1=0  
    def area(self,a,b,c):
        s=(a+b+c)/3
        area1=(s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(area1)

    
    class ParentClass:
    def getLengthOfSideOfTriangle(self):
        values = ["first", "second", "third"]
        sides = []
        for index in values :
            inputValue = input("Please provide length of {} side of a triangle".format(index))
            sides.append((inputValue))
        return sides

class ChildClass(ParentClass):
    def getAreaOfTriangle(self, lengthOfSideOfTriangle):
        a = int(lengthOfSideOfTriangle[0])
        b = int(lengthOfSideOfTriangle[1])
        c = int(lengthOfSideOfTriangle[2])
        
        s = (a + b + c)/2
        
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(area)
        
childClass = ChildClass()
lengthOfSideOfTriangle = childClass.getLengthOfSideOfTriangle()
childClass.getAreaOfTriangle(lengthOfSideOfTriangle)


# # 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[ ]:


def LongestWord():
    txt = input('please enter list of words')
    longest =0
    for f in txt.split(','):
        if len(f) > longest:
            longest=len(f)
            longest_word=f
            
    print(longest_word)
        

LongestWord()


# # 1.3 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[ ]:



l=[]
def lenofwords():
    txt = input('please enter list of words')
    longest =0
    for f in txt.split(','):
        g=len(f)
        l.append(g)
    print(l)
    
lenofwords()


# # 1.4 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# In[ ]:



def vowelchecking(x):
    for t in x:
        if t in ['a','e','i','o','u','A','E','I','O','U']:
             return True
        else:
             return False
   
#calling Function
vowelchecking(input('Please enter any alphabet'))

