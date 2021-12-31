#!/usr/bin/env python
# coding: utf-8

# # QUESTION #1 
# 1) Write a Python program to print the following string in a specific format:
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# 
# 

# In[1]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# # QUESTION #2
# Write a python program to get the python version you are using.

# In[2]:


import sys
print(sys.version)


# # QUESTION #3
# 
# Write a python program to display current day and time.

# In[3]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (str(now))


# # QUESTION #4
# 
# Write a python program to display current day and time.

# In[4]:


r = input("Please type radius of your circle ")
r = float(r)
pi = (3.14)
area = pi * r ** 2
print("Area of the circle is", area)


# # QUESTION #5
# 
# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

# In[5]:


first_name = input('Please enter first name:')    
last_name = input('Please enter last name:')    
print(last_name,first_name)


# # QUESTION #6
# write a python program which takes two inputs from user and print them addition.

# In[6]:


a=int(input('ENTER THE VALUE OF a:'))
b=int(input('ENTER THE VALUE OF b:'))
print('ADDITION=',a+b)


# In[ ]:




