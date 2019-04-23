
# coding: utf-8

# ### Python 1,2,3,4 & 5 :Assignment 1

# ### 2.1. Problem Statement:  PYTHON 1 
#  
# **Question - 1 .Install Jupyter notebook and run the first program and share the screenshot of the output.**

# **Answer**

# In[2]:


a = 'I am Pallab Panda'
b='A Data Science student'
print(a+'.'+b)


# **Note - I have shared the screen shot of first question on given repository.**

# **Question- 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line)**

# **Answer**

# In[19]:


x=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        x.append(i)
print (x)


# ** Question - 3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name**

# **Answer**

# In[3]:


x = input('Your first name please : ')
y = input('Your last name please : ')
print(x[::-1],y[::-1])


# **Question - 4.Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 π r^3**

# **Answer**

# In[20]:


diameter = 12 #diameter
radius = (diameter/2) #radius
pi = (22/7) #3.14159
volume= 4/3*pi*radius**3
print(volume)


# ### 2.2. Problem Statement: PYTHON 2

# **Question -1.Write a program which accepts a sequence of comma-separated numbers from console and generate a list.**

# **Answer**

# In[21]:


values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)


# **Question - 2. Create the below pattern using nested for loop in Python.**

# **Answer**

# In[6]:


for i in range(1,6,1):
    print('*'*i)
for i in range(4,0,-1):
    print('*'*i)


# **Question - 3. Write a Python program to reverse a word after accepting the input from the user.**

# **Answer**

# In[7]:


a = input('Input word : ')
print(a[::-1])


# **Question - 4. Write a Python Program to print the given string in the format specified in the sample output.**
# 
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
# 
# **Sample Output:**
# 
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, ! SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens:
# 

# **Answer**

# In[8]:


a = ("WE, THE PEOPLE OF INDIA, \n\t"" having solemnly resolved to constitute India into a SOVEREIGN,!\n\t\t"" SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t ""and to secure to all its citizens")
print(a)


# ### 2.3. Problem Statement: PYTHON 3

# **Question - 1.1. Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()**

# **Answer**

# In[2]:


def myreduce(a,b):
    aa = 0
    for i in range(a,b):
        aa = aa+i
    print (aa)

myreduce(1,15)


# **Question - 1.2. Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()**

# **Answer**

# In[3]:


def myfilter(f,s):
    x = []
    for i in s:
        if i<0:
            x.append(i)
    return x

print(list(myfilter((lambda x:x<0),range(-10,10,1))))


# **Questio 2. Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists.**
# 
# **['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# 
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
# 
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 
# 
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# 
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]**

# In[4]:


# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#list("ACADGILD")

x = list("ACADGILD")
[i for i in x]


# In[5]:


# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
a=['x','y','z']
[i*j for i in a for j in range(1,5)]


# In[6]:


# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
a=['x','y','z']
[i*j for i in range(1,5) for j in a]


# In[7]:


# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
a = list(range(2,5))
[[i+j] for i in a for j in range(3) ]


# In[8]:


# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
a = list(range(2,6))
[[i+j for i in a] for j in range(0,4)]


# In[24]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print(str(result))


# **Question - 3. Implement a function longestWord() that takes a list of words and returns the longest one.**

# **Answer**

# In[26]:


from functools import reduce
list_words = ["This","is","a","python","assignment"]

# Function to compare and reduce list to the result
def longestWord(list_words):
 return reduce( (lambda x,y:y if len(y) > len(x) else x), list_words )

print ('Longest word in array ["This","is","a","python","assignment"] => ' + longestWord(list_words) )


# ### 2.4. Problem Statement: PYTHON 4

# **1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.**

# **Answer**

# In[10]:


class Triangle:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    
    def area(self):
        s=(self.side1+self.side2+self.side3)/2
        return ((s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

a=float(input('Enter the value of side 1: '))
b=float(input('Enter the value of side 2: '))
c=float(input('Enter the value of side 3: '))
print('Area of the triangle',Triangle(a,b,c).area())


# **1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.**

# **Answer**

# In[1]:


class list_Utilities:
 def __init__(self, wordlist):
  self.wordlist = wordlist
  print ("Initialised list_Utilities object")

 def filter_long_words(self, n):
  return list(filter(lambda x:len(x) > n, self.wordlist))

instance = list_Utilities(["This","is","a","beautiful","day"])
print ("New List of Words  => " + str(instance.filter_long_words(3)) ) 


# **Question - 2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]**

# **Answer**

# In[13]:


def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
words = ['ab','cde','erty']
map_to_lengths_for(words)


# **Question - 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.**

# **Answer**

# In[15]:


def vowel_or_not(x):
    vowels=['a','e','i','o','u']
    if x in vowels:
        return True
    return False

vowel_or_not('b')


# ### 2.5. Problem Statement: PYTHON 5

# **Question - 1. Write a function to compute 5/0 and use try/except to catch the exceptions.**

# **Answer**

# In[16]:


def divide_function(x,y):
    try:
        z=x/y
        print(z)
    except:
        y=0
        print('infinite')

divide_function(5,0)


# **Question - 2. Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].**
# 
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# 
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

# **Answer**

# In[17]:


sub = ['Americans','Indians']
ver = ['play','watch']
obj = ['baseball','cricket']
a = [' '.join([i,j,k]) for i in sub for j in ver for k in obj]
#a
for l in a:
    print(l)

