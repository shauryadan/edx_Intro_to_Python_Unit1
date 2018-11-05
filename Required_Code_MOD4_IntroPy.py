
# coding: utf-8

# #  Module 4 Required Coding Activity  
# Introduction to Python Unit 1 
# 
# The activity is based on modules 1 - 4 and is similar to the Jupyter Notebooks **`Practice_MOD04_1-6_IntroPy.ipynb`** and **`Practice_MOD04_1-7_IntroPy.ipynb`** which you may have completed as practice.  This activity is a new version of the str_analysis() function.
# 
# | Some Assignment Requirements |
# |:-------------------------------|
# |This program requires the use of<ul><li>**`while`** loop to get non-empty input</li><li>**`if, else`**</li><li>**`if, else`** (nested)</li><li>**`.isdigit()`** check for integer only input</li><li>**`.isalpha()`** check for alphabetic only input</li></ul><br/>The program should **only** use code syntax covered in modules 1 - 4.<br/><br/>The program must result in printed message analysis of the input.  |
# 
# 
#   
# ## Program: `str_analysis()` Function  
# 
# Create the str_analysis() function that takes 1 string argument and returns a string message.  The message will be an analysis of a test string that is passed as an argument to str_analysis(). The function should respond with messages such as:  
# - "big number"
# - "small number"
# - "all alphabetic"
# - "multiple character types"
# 
# The program will call str_analysis() with a string argument from input collected within a while loop.  The while loop will test if input is empty (an empty string "") and continue to loop and gather input until the user submits at least 1 character (input cannot be empty).  
# 
# The program then calls the str_analysis() function and prints the **return** message.
# 
# 
# 
# #### Sample input and output:  
# enter nothing (twice) then enter a word  
# ```
# enter word or integer: 
# enter word or integer: 
# enter word or integer: Hello
# "Hello" is all alphabetical characters!
#   
# ```  
# -----    
#   
# alphabetical word input 
# ```
# enter word or integer: carbonization
# "carbonization" is all alphabetical characters!
#   
# ```  
# -----     
#    
# numeric inputs
# ```
# enter word or integer: 30
# 30 is a smaller number than expected
# 
# enter word or integer: 1024
# 1024 is a pretty big number
# ```  
# -----  
# 
# 
# ### loop until non-empty input is submitted  
# This diagram represents the input part of the assignment - it is the loop to keep prompting the user for input until they submit some input (non-empty).  
# 
# ![image of while Loop with nested if statements described in bulleted text above](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/input_loop_sketch.png)  
# 
# Once the user gives input with characters use the input in calling the str_analysis() function.
# 
# ### Additional Details
# In the body of the str_analysis() function:
# - Check `if` string is digits  
#   - if digits: convert to `int` and check `if` greater than 99  
#     - if greater than 99 print a message about a "big number"  
#     - if not greater than 99 print message about "small number"  
#   - check if string isalpha then (since not digits)
#     - if isalpha print message about being all alpha
#   - if not isalpha print a message about being neither all alpha nor all digit  
#     
# call the function with a string from user input 
# - Run and test your code before submitting

# In[21]:


# [ ] create, call and test the str_analysis() function  
# then PASTE THIS CODE into edX  


def str_analysis(string):
    if string.isdigit():
        if int(string) > 99:
            print("big number")
        else:
            print("small number")
    elif string.isalpha():
        print("String is all alpha")
    elif string == "":
        usr_ip = input("Enter word or digit: ")
        str_analysis(usr_ip)
    else:
        print("String is neither all digit nor all alpha")
        
usr_ip = input("Enter word or digit: ")
while str_analysis(usr_ip) == "":
    str_analysis(usr_ip)






# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 4 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+4T2017/course)    
# 
# # Important:  [How to submit the code in edX by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+1T2017/wiki/Microsoft.DEV236x.3T2018/paste-code-end-module-coding-assignments/)

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
