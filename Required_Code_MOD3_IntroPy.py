
# coding: utf-8

# #  Module 3 Required Coding Activity  
# Introduction to Python Unit 1 
# 
# This is an activity based on code similar to the Jupyter Notebook **`Practice_MOD03_1-4_IntroPy.ipynb`** and **`Practice_MOD03_1-5_IntroPy.ipynb`** which you may have completed as practice.
# 
# > **NOTE:** This program requires the use of **`if, elif, else`**, and casting between strings and numbers. The program should use the various code syntax covered in module 3.  
# >  
# >The program must result in print output using numeric input similar to that shown in the sample below.
# 
# ## Program: Cheese Order    
# 
# - set values for maximum and minimum order variables  
# - set value for price variable
# - get order_amount input and cast to a number  
# - check order_amount and give message checking against  
#   - over maximum
#   - under minimum
# - else within maximum and minimum give message with calculated price 
# 
# 
# Sample input and output:
# ```
# Enter cheese order weight (numeric value): 113
# 113.0 is more than currently available stock
# ```
# 
# ```
# Enter cheese order weight (numeric value): .15
# 0.15 is below minimum order amount
# ```  
# 
# ```
# Enter cheese order weight (numeric value): 2
# 2.0 costs $15.98
# ```  

# In[3]:


# [ ] create, call and test 
# then PASTE THIS CODE into edX
max_order = 100
min_order = 0.25
price = 55.5

order_amount = float(input("Enter order amount: "))

if order_amount > 100:
    print(order_amount, "is more than currently available stock")
elif order_amount < 0.25:
    print(order_amount, "is below minimum order amount")
else:
    print(order_amount, "costs", order_amount * price)


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 3 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+4T2017/course)  
# 
# # Important:  [How to submit the code in edX by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+1T2017/wiki/Microsoft.DEV236x.3T2018/paste-code-end-module-coding-assignments/)

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
