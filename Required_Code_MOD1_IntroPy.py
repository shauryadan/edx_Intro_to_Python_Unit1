
# coding: utf-8

# #  Module 1 Required Coding Activity  
# Introduction to Python Unit 1
# 
# This is an activity from the Jupyter Notebook **`Practice_MOD01_1-2_IntroPy.ipynb`** which you may have already completed.
# 
# > **NOTE:** This program requires print output and code syntax used in module 1
# 
# | Some Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires `print` output and using code syntax used in module 1 such as variable assignment, `input`, `in` keyword, `.lower()` or `.upper()` method  |  
# 
# 
# ## Program: Allergy Check  
# 
# 1. **[ ]** get user **`input`** for categories of food eaten in the last 24 hours  
#  save in a variable called **input_test**  
#  *example input*
#  [![01 02 practice Allergy-input](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_input.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65qzFD5CGvv95-ijg)
# &nbsp;  
# 2. **[ ]** print **`True`** if "dairy" is in the **input_test** string  
# **[ ]** Test the code so far  
# &nbsp;
# 3. **[ ]** modify the print statement to output similar to below  
# *example output*
# [![01 02 Allergy output](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/eaten_output.gif) ](https://1drv.ms/i/s!Am_KPRosgtaij65rET-wmlpCdMX7CQ)  
# Test the code so far trying input including the string "dairy" and without  
# &nbsp;  
# 
# 4. **[ ]** repeat the process checking the input for "nuts", **challenge** add "Seafood" and "chocolate"  
# **[ ]** Test your code  
# &nbsp;  
#   
# 5. **[ ] challenge:** make your code work for input regardless of case, e.g. - print **`True`** for "Nuts", "NuTs", "NUTS" or "nuts"  
# 

# In[8]:


# Create Allergy check code
# then PASTE THIS CODE into edX

# [ ] get input for input_test variable
input_test = input("enter food categories eaten in last 24 hrs: ")

# [ ] print "True" message if "dairy" is in the input or False message if not
print('It is', "dairy".lower() in input_test, 'that "' + input_test + '" contains ' + 'dairy'.lower() )

# [ ] print True message if "nuts" is in the input or False if not
print('It is', "nuts".lower() in input_test, 'that "'+ input_test + '" contains ' + 'nuts'.lower()  )

# [ ] Challenge: Check if "seafood" is in the input - print message
print('It is', "seafood".lower() in input_test, 'that "' + input_test + '" contains ' + 'seafood'.lower() )

# [ ] Challenge: Check if "chocolate" is in the input - print message
print('It is', "chocolate".lower() in input_test, 'that "' + input_test + '" contains ' + 'chocolate'.lower() )


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 1 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+4T2017/course)  
#     
# 
# # Important:  [How to submit the code in edX by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+1T2017/wiki/Microsoft.DEV236x.3T2018/paste-code-end-module-coding-assignments/)

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
