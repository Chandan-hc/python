#!/usr/bin/env python
# coding: utf-8

# # strings

# #### a) Concatenation (+) and Repetition (*)

# In[25]:


#1
institute = 'Edukron'
focus_area = 'DataScience'
  
full_title = institute + ": " + focus_area
print(f"1. FULL_TITE:{full_title}")


# In[7]:


#2
course_name = "mern stack"
message = "Welcome to " + institute + "'s " + course_name + " course!"
print(f"2. Welcome message: {message}") 


# In[8]:


#3
separator = ("-*=") * 5
print(f"3. Separator: {separator}")


# In[10]:


#4
keyword = " pandas "
emphasized = keyword * 13
print(f"4. Emphasized keyword: {emphasized}")


# In[11]:


#5
base_path = "/courses/"
course_id = "DA101"
full_path = base_path + course_id
print(f"5. Simple path: {full_path}")


# In[12]:


#6
student_name = "jose"
username_suffix = "@edukron.com"
email = student_name + username_suffix
print(f"6. Student email: {email}")


# In[16]:


#7
heading = "Course Modules"
underline = "=" * len(heading) 
print(f"7. Heading:\n{heading}\n{underline}")


# In[17]:


#8
part1 = "start "
part2 = "learning "
part3 = "Now!"
call_to_action = part1 + part2 + part3
print(f"8. Call to action: {call_to_action}")


# In[19]:


#9
empty_repeated = "_" * 100
print(f"9. Repeating empty string: '{empty_repeated}'") 


# In[23]:


#10
message = "ALERT! "
no_alerts = message * 0
print(f"10. Repeating zero times: '{no_alerts}'") 


# #### B len()

# In[ ]:


institute = "Edukron"
course_slogan = "Learn Data Engineering with Real-Time Projects"
tech_stack = "Azure DevOps and Python"


# In[27]:


# 1. Length of the institute name
name_length = len(institute)
print(f"1. Length of '{institute}': {name_length}")


# In[28]:


# 2. Length of the course slogan
slogan_length = len(course_slogan)
print(f"2. Length of slogan: {slogan_length}")


# In[30]:


#3. Length of the tech stack description
stack_length = len(tech_stack)
print(f"3. Length of tech stack: {stack_length}")


# In[31]:


# 4. Length of an empty string
empty_len = len("")
print(f"4. Length of empty string: {empty_len}")


# In[32]:


# 5. Length of a string with only spaces
spaces = "   "
spaces_len = len(spaces)
print(f"5. Length of '{spaces}': {spaces_len}")


# In[34]:


#6. Using len() for validation (e.g., minimum password length)
password = "pass"
min_len = 8
if len(password) < min_len:
   print(f"6. Password '{password}' is too short (min {min_len} chars required).") 


# In[35]:


# 7. Length of a string containing numbers and symbols
complex_str = "Batch #101!"
complex_len = len(complex_str)
print(f"7. Length of '{complex_str}': {complex_len}") 


# In[36]:


# 8. Length after concatenation
combined = institute + tech_stack # "EdukronAzure DevOps and Python"
combined_len = len(combined)
print(f"8. Length of combined string: {combined_len}")


# In[38]:


#9. Length of a single character string
char_str = "A"
char_len = len(char_str)
print(f"9. Length of '{char_str}': {char_len}")


# In[ ]:


# 10. Length of a multi-line string (includes newline characters)
multi_line = """Line 1
Line 2"""
multi_len = len(multi_line)
print(f"10. Length of multi-line string:\n'''{multi_line}'''\nis: {multi_len}")

