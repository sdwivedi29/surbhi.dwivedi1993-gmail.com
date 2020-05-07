#!/usr/bin/env python
# coding: utf-8

# # Pandas assignment_data cleaning :

# In[ ]:


1.Introduction
This assignment will help you to consolidate the concepts learnt in the session.
2.Problem Statement
It happens all the time: someone gives you data containing malformed strings,
Python, lists and missing data. How do you tidy it up so you can get on with the
get_ipython().run_line_magic('pinfo', 'analysis')
Take this monstrosity as the DataFrame to use in the following puzzles:
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

1. Some values in the the FlightNumber column are missing. These numbers are
meant to increase by 10 with each row so 10055 and 10075 need to be put in
place. Fill in these missing numbers and make the column an integer column
(instead of a float column).
2. The From_To column would be better as two separate columns! Split each
string on the underscore delimiter _ to give a new temporary DataFrame with
the correct values. Assign the correct column names to this temporary
DataFrame.
3. Notice how the capitalisation of the city names is all mixed up in this
temporary DataFrame. Standardise the strings so that only the first letter is
uppercase (e.g. "londON" should become "London".)
4. Delete the From_To column from df and attach the temporary DataFrame
from the previous questions.
5. In the RecentDelays column, the values have been entered into the
DataFrame as a list. We would like each first value in its own column, each

second value in its own column, and so on. If there isn't an Nth value, the value
should be NaN.
Expand the Series of lists into a DataFrame named delays, rename the columns
delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
with delays.
Note: Solution


# In[4]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm',

'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

df


# 1. Some values in the the FlightNumber column are missing. These numbers are
# meant to increase by 10 with each row so 10055 and 10075 need to be put in
# place. Fill in these missing numbers and make the column an integer column
# (instead of a float column).

# 1. Some values in the the FlightNumber column are missing. These numbers are
# meant to increase by 10 with each row so 10055 and 10075 need to be put in
# place. Fill in these missing numbers and make the column an integer column
# (instead of a float column).

# In[5]:




df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

df['FlightNumber']


# In[ ]:





# In[ ]:


df


# 2. The From_To column would be better as two separate columns! Split each
# string on the underscore delimiter _ to give a new temporary DataFrame with
# the correct values. Assign the correct column names to this temporary
# DataFrame.

# In[7]:


df['From_To']
t=df.copy()

t[['From','To']]= t.From_To.str.split("_",expand=True)
t


# 3. Notice how the capitalisation of the city names is all mixed up in this
# temporary DataFrame. Standardise the strings so that only the first letter is
# uppercase (e.g. "londON" should become "London".)

# In[8]:


t.From = t.From.str.capitalize()
t.To = t.To.str.capitalize()
t


# In[9]:


t.From_To=t.From_To.str.capitalize()
t


# 4. Delete the From_To column from df and attach the temporary DataFrame
# from the previous questions.

# In[10]:


df


# 4. Delete the From_To column from df and attach the temporary DataFrame
# from the previous questions.

# In[11]:


df.drop('From_To',axis=1,inplace=True)
df


# In[12]:


df['From_To']=t['From_To']
df


# 5. In the RecentDelays column, the values have been entered into the
# DataFrame as a list. We would like each first value in its own column, each
# 
# second value in its own column, and so on. If there isn't an Nth value, the value
# should be NaN.
# Expand the Series of lists into a DataFrame named delays, rename the columns
# delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df
# with delays.
# Note: Solution

# In[15]:


delays = df['RecentDelays'].apply(pd.Series)

delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]

df = df.drop('RecentDelays', axis=1).join(delays)

df


# In[ ]:




