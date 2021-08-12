#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("hello world")


# # variable

# In[3]:


# data/values can be stored in temprory storage spaces called as variables.


# In[4]:


#student = "Ram","shyam","amit".
#here "student" Work as variable.
# A variables ahas always a name and address.


# In[8]:


student = "ram","shyam","Amit"
student


# In[9]:


(id(student))


# In[11]:


(type(student))


# In[10]:


# command for:
# for getting data memory or address-
#print(id(variable name))
# for getting data type-
#print(type(variable name))


# In[12]:


student = "ram"


# In[13]:


student


# In[14]:


(type(student))


# In[15]:


# that means variables are temprory and we can it later.


# In[16]:


# every variable is assocciated with data type.
#data type are:

#Interger(int)= 100,522,546

#float = 4.10,9.5

#Boolean(bool)= TRUE,FALSE

#string(str)= "tom","sam"

#complex = 7+4i,9+8i


# In[21]:


a1 = 10
a1


# In[22]:


(type(a1))


# In[23]:


a1 = 3.4
a1


# In[24]:


(type(a1))


# In[25]:


a1 = "sam"
a1


# In[26]:


(type(a1))


# In[27]:


a1 = True
a1


# In[28]:


(type(a1))


# In[32]:


a1 = 3+4j
a1


# In[30]:


(type(a1))


# In[33]:


# in python i is replaced by j in complex data type.


# # operators in python

# In[34]:


# operators in python:

# 1.Relational operator
# 2.Arithmatic operator.
# 3.Logical operator.


# In[35]:


# Arithmetic operators: +,-,/,*


# In[36]:


a = 10
b = 15


# In[37]:


a + b


# In[38]:


a - b


# In[39]:


b - a


# In[40]:


a / b


# In[41]:


b / a


# In[42]:


a * b


# In[43]:


# Relational operators: <,>,==,!=


# In[44]:


a = 50
b = 100


# In[45]:


a < b


# In[46]:


b > a


# In[47]:


a == b


# In[48]:


a != b


# In[49]:


b != a


# In[50]:


# Logical operators : ( &,|)


# In[51]:


a = True
b = False


# In[52]:


#for & operators


# In[53]:


a & a


# In[54]:


a & b


# In[55]:


b & a


# In[56]:


b & b


# In[57]:


# for or operators(|)


# In[58]:


a | a


# In[59]:


a | b 


# In[61]:


b | a


# In[62]:


b | b


# In[63]:


# or(|) operators give preference to True.


# # python token

# In[64]:


# python token
# >>> smallest meaningfull component in program is called as python token.

# 1.keywords
# 2.identifiers
# 3.Literals
# 4.Operators


# In[65]:


# keywords:
 #False,None,True,and,as,class,continue,def,del,elif,finally,from,for,global,if,is,lambda,nonlocal,not,or,return,try,while,with,yield.


# In[66]:


# Identifiers are the names of variables,functions or objects.

# Rules:
# 1.No special character expect underscore(_)
# 2.Identifiers are case sensitive.
# 3.First letter cannot be start with digits.


# In[67]:


# example of case sesitive:-


# In[68]:


student = "martha"


# In[72]:


Student = "sony"


# In[70]:


student


# In[74]:


Student


# In[75]:


# Literals:-
# Literals are constant values that is stored in variables and cant be changed.

# Example:
# a = "hello world"
# here "a" is variable and "hello world" is a literal that cant be changed.


# In[78]:


# python stings(str):
# strings are sequence of characters enclosed with single quotes(' '),double quotes(" "),or triple quotes(''' ''')

# Examples:
# 1.'hello world'
# 2." python expert"
# 3.''' I am killing python'''


# In[ ]:


# Example of single quote string.


# In[79]:


str1 = 'this is my first string'
str1


# In[80]:


(type(str1))


# In[81]:


# Example of double quote string.


# In[82]:


str2 = " this is my second string"
str2


# In[83]:


(type(str2))


# In[84]:


# Example of triple quote string.


# In[85]:


str3 = '''
this stings
has
lots of
line in it
'''
str3


# In[86]:


(type(str3))


# In[87]:


# (\n) means a new line form.


# In[88]:


# Extracting individual characters in pyton by help of indexing.


# In[109]:


my_string = "my name is john"
my_string[0]


# In[100]:


my_string[-1]


# In[103]:


my_string[3:10]


# In[104]:


# finding length of string use: 

#len(variables)


# In[105]:


len(my_string)


# In[110]:


# converting string to lower case: 

#variables.lower()


# In[111]:


my_string = "MY NAME IS KHAN"
my_string.lower()


# In[112]:


# for converting to upper from lower case:
# variable.upper()


# In[59]:


my_string = "my name is khan"
my_string.upper()


# In[116]:


# Replacing a sub string:
# Variable.replace('character want to replace of','character want to replace with')


# In[117]:


# example:


# In[118]:


my_string = "my name is khan"
my_string.replace('y','a')


# In[119]:


# For counting the substring repeatation:
# variable.count('word that you want to count')


# In[124]:


my_new_string = "my my name is khan"
my_new_string.count('my')


# In[125]:


# function for finding the index vanlue of first character of any substring.
# variable.find('substring')


# In[135]:


s1 = "my name is khan"
s1.find('khan')


# In[127]:


# 11 is a index value of k i.e the first character of substring 'khan'.


# In[128]:


# function for spliting a string:
# variable.split('spliting character')


# In[130]:


fruit = "I like mango,banana,orange"
fruit


# In[133]:


fruit.split(',')


# # data structure in python.

# In[1]:


# Data structure in python:
# 1.tuple
# 2.list
# 3.Dictonary
# 4.set


# # tuple  (replace and split fuctions cant work in tuple)

# In[2]:


# Tuple is an orderd collection of elements enclosed with round brackets ()
#tuples are immutable.
# tup1 = (1,'a',3.4,True)


# In[4]:


tup1 = (1,3.4,True,'arnold',3-7j)
tup1


# In[5]:


(type(tup1))


# In[6]:


# Extracting individual elements by indexing for tuple:


# In[7]:


tup1 = (1,3.4,True,"arnold",3-7j)
tup1[0]


# In[9]:


tup1[-1]


# In[13]:


tup1[1:4]


# In[17]:


# we cant change the value of tuple after assigning and if we do then we get type error.


# In[18]:


# example:


# In[19]:


tup2 = ('ram',233,7+2j,5.6)
tup2[1] = 255


# In[20]:


# for finding lenght in tuple:


# In[27]:


tup2 = ('ram',233,7+2j,5.6,5.6)


# In[28]:


len(tup2)


# In[ ]:


# for counting characters in tuple:


# In[30]:


tup2.count(5.6)


# In[33]:


# for concatenating or merge two tuple:


# In[34]:


tup1 = (1,2,3)
tup2 = (4,5,6)


# In[35]:


tup1+tup2


# In[36]:


# similarly


# In[37]:


tup3 = (1,5.6,'ram')
tup4 = (5,6.8,'dharam')


# In[38]:


tup3+tup4


# In[39]:


len(tup3+tup4)


# In[40]:


tup4+tup3


# In[41]:


# for Repeating tuple element: *


# In[43]:


# example


# In[55]:


tup = ('sparta',300)
tup*5


# In[56]:


# for concatenating and reapeting tuple at same time.


# In[57]:


tup1 = ('sparta',300)
tup2 = (1,2,3)


# In[58]:


tup1*2 + tup2


# In[63]:


# for finding minimum values:-  min(variable name)


# In[64]:


# Example


# In[66]:


tup1 = (1,2,3,4,5)
min(tup1)


# In[67]:


# for finding maximum value in tuple elements.


# In[68]:


# Examples


# In[69]:


max(tup1)


# # list in python

# In[70]:


# list is also an ordered collection of elelments enclosed within []


# In[71]:


# diffrence between tuple and list is ,tuple is immutable data stucture but list is mutable or editable data structure.


# In[72]:


l1 = [120,3.55,'sparta',7+9j]
l1


# In[73]:


(type(l1))


# In[74]:


# extracting in list by using indexing.


# In[76]:


l1 = [1,2.5,'sparta']
l1


# In[77]:


l1[0]


# In[80]:


l1[-1]


# In[79]:


l1[0:2]


# In[81]:


# way to modifying a list becuase it is mutable:


# In[82]:


# changing an element at zeroth index.


# In[86]:


l1 = [1,2.5,'sparta']
l1[0] = 2
l1


# In[ ]:


# for appending an element in list use :- variable.append('elemnt to append')


# In[98]:


# example:


# In[100]:


l1 = [1,2.5,'sparta']
l1.append(1)
l1


# In[101]:


#for popping the last element in list use :- variable.pop()


# In[ ]:


# Example:


# In[107]:


l1 = [1,2.5,'sparta']
l1.pop()


# In[103]:


l1


# In[ ]:


# 2nd example


# In[115]:


l2 = [1,6.5,'parrot','jack ma']
l2


# In[116]:


l2.pop(1)


# In[117]:


l2


# In[118]:


# reversing a list:- variable.reverse()


# In[119]:


# Example:


# In[120]:


l2 = [1,6.5,'parrot','jack ma']


# In[135]:


l2.reverse()


# In[124]:


l2


# In[129]:


# Inserting an element at a specifc index:- variable.insert('where after u want to insert','what you want to insert')


# In[ ]:


l2 = [1,6.5,'parrot','jack ma']


# In[131]:


l2.insert(1,'sparta')


# In[133]:


l2


# In[136]:


# sorting in list:- variable.sort()


# In[139]:


l2 = ['banana','apple','lichi','guava']


# In[144]:


l2.sort()


# In[141]:


l2


# In[148]:


# 2nd example:


# In[153]:


l2 = [2,3,5,8,9,11,15,4,22,6]


# In[154]:


l2.sort()


# In[155]:


l2


# In[156]:


# concatenating list:


# In[160]:


l1 = [1,2,3]
l2 = ['a','b','c']


# In[163]:


l1 + l2


# In[164]:


# Repeating element:


# In[168]:


l1 = [1,2,3]


# In[169]:


l1*3


# In[172]:


l2 = [10,20,30]


# In[173]:


l1*3 + l2


# # Dictionary in python

# In[1]:


# dictionary is an unordered collection of keys-values pairs enclosed within {}
# Keys should be imutable and uniqe
# dictionary is mutable data stucture.


# In[2]:


fruits = {'apple':100,"guava":50,"mango":90,'lichi':150}


# In[3]:


# "apple" is key and 100 is value.


# In[4]:


# Extracting keys in dictionary


# In[6]:


fruits = {'apple':100,"guava":50,"mango":90,'lichi':150}


# In[7]:


fruits.keys()


# In[8]:


fruits.values()


# In[9]:


# Modification in dictionary


# In[10]:


# Adding an element


# In[11]:


fruits = {'apple':100,"guava":50,"mango":90,'lichi':150}


# In[12]:


fruits['banana'] = 120


# In[13]:


fruits


# In[14]:


# Changing an existing element


# In[15]:


fruits = {'apple':100,"guava":50,"mango":90,'lichi':150}


# In[16]:


fruits['apple'] = 50


# In[17]:


fruits


# In[18]:


# Update one dict into another


# In[19]:


dict1 = {"apple":150,"mango":120,"guava":80}
dict2 = {"lichi":50,"banana":50,"papaya":30}


# In[20]:


dict1.update(dict2)


# In[21]:


dict1


# In[22]:


# Poping an element in dict


# In[23]:


fruits = {'apple':100,"guava":50,"mango":90,'lichi':150}


# In[25]:


fruits.pop('apple')


# In[26]:


fruits


# # Set in python

# In[27]:


# Set is an unordered and unindexed mutable.
# cannot repeat element in set


# In[28]:


s1 = {1,2.5,'mango',4+5j,'b',20}


# In[29]:


# add element in set


# In[30]:


s1.add("hello")


# In[31]:


s1


# In[32]:


# add multiple element 


# In[33]:


s1 = {1,2.5,'mango',4+5j,'b',20}


# In[35]:


s1.update([10,20,30])


# In[36]:


s1


# In[37]:


# Remove element in set


# In[38]:


s1 = {1,2.5,'mango',4+5j,'b',20}


# In[39]:


s1.remove(2.5)


# In[40]:


s1


# In[41]:


# Union or merging to sets into each other


# In[43]:


s1 = {1,2,3}
s2 = {'a','b','c'}


# In[44]:


s1.union(s2)


# In[45]:


# Intersecting elements from two sets.


# In[46]:


s1 = {1,2,3,4,5,6,}
s2 = {3,4,5,6,7,8,}


# In[47]:


s1.intersection(s2)


# # Decision making statement

# In[48]:


# use of if,elif and else.


# In[49]:


# Pseudo code
# if (condition):
#   print('statement')
# elif (condition):
#   print('statement')
# else:
#   print('statement')


# In[50]:


# example:


# In[51]:


a = 20
b = 30
c = 40


# In[52]:


if (a>b)&(a>c):
    print('a is greatest')
elif (b>a)&(b>c):
    print('b is greatest')
else:
    print('c is greatest')


# In[53]:


# Example two


# In[54]:


a = 20
b = 40


# In[56]:


if (a<b):
    print('b is greater than a')
else:
    print('a is greater than b')


# In[58]:


# how to use 'if' with tuple,'list' and 'dictionary'


# In[60]:


# using if with 'tuple'


# In[71]:


# Example


# In[72]:


tup1 = ('a','b','c')


# In[70]:


if ('a') in tup1:
    print('a is present')


# In[73]:


# Example2


# In[74]:


tup1 = ('a','b','c')


# In[75]:


if ('z') in tup1:
    print('a is present')
else:
    print('z is not present')


# In[76]:


# If with list


# In[86]:


# Example


# In[90]:


fruits = ["mango","banana","papaya","lichi"]


# In[91]:


if ("lichi")in fruits:
    print("lichi is present in list")


# In[92]:


# Example 2


# In[93]:


fruits = ["mango","banana","papaya","lichi"]


# In[94]:


if ("guava")in fruits:
    print("guava is present in list")
else:
    print("guava is not present")


# In[95]:


# Example 3


# In[96]:


l1 = ['a','b','c']


# In[105]:


if (l1[0]=='a'):
 l1[0]='d'


# In[106]:


l1


# In[107]:


# using 'if' with dictionary


# In[108]:


# Example


# In[125]:


dict = {'key1':10,'key2':20,'key3':30}


# In[130]:


if dict['key3']==30:
    dict['key3']=dict['key3']+100


# In[131]:


dict


# # loops in python

# In[133]:


# looping statement are used to repeat a task multiple time


# In[134]:


# Examples


# In[136]:


# 1.Keep filling bucket with mug untill its full
# 2.Keep repeating your favourite song untill app closed
# 3.Get your salary at the end of month.


# ## while loop

# In[137]:


# for getting number 1 to 10


# In[138]:


# Example


# In[139]:


i = 1
while i<=10:
    print(i)
    i=i+1


# In[3]:


i=1
n=2
while i<=10:
    print(n , " * " ,i, " = ", n*i)
    i=i+1


# ## Use while loop with list:

# In[6]:


l1 = [1,2,3,4,5]
i = 0
while i<len(l1):
    l1[i]=l1[i]+100
    i=i+1


# In[8]:


l1


# In[1]:


# Example3:


# In[4]:


count = 0
while (count<5):
    print('i m in the loop')
    count = count + 1


# In[5]:


# Example4: make a table bar- 


# In[8]:


number = int(input('enter a number:'))
count = 1
while count <= 10:
    product = number*count
    print(number, 'x', count, '=', product)
    count = count + 1


# # for loop

# In[9]:


# for loop is used to iterate over a sequence(tuple,list and dictionary)


# In[10]:


# example:


# In[15]:


l1 = ['mango','banana','papaya','lichi']
for i in l1:
    print(i)


# In[16]:


# Example2:


# In[21]:


l1 = ['mango','banana','papaya','lichi']
l2 = [20,50,80,100]
for i in l1:
    for j in l2:
     print(i,j)


# # Function in programing

# In[27]:


# Function is block of code which perform a specific task:


# In[28]:


# Example will be online banking where we deposite money,withdraw money and camn check balance at the same machine and ATM.


# In[29]:


# def is used when u start creating fuction.


# In[30]:


# Example:


# In[33]:


def hello():
    print('hello world')


# In[38]:


hello()


# In[39]:


# example2:


# In[47]:


def plus_10(x):
    return(x + 10)


# In[48]:


plus_10(7)


# In[59]:


def even_odd(x):
    if x%2==0:
     print(x, "number is even")
    else:
     print(x, 'number is odd')


# In[58]:


even_odd(10)


# In[60]:


even_odd(5)


# # lambda function

# In[61]:


# A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.
# Normally we dont need to define lambda fuction.


# In[62]:


# examples:


# In[65]:


g = lambda x: x*x*x


# In[70]:


g(10)


# In[67]:


# Normally we use lambda fiuntion with other function that is filter,map and radio function


# In[68]:


# Lambda with filter


# In[79]:


l1 = [10,15,20,25,30,35,80,85]
final_list = list(filter(lambda x:(x%2!=0),l1))


# In[80]:


final_list


# In[81]:


# Lambda with map


# In[82]:


l1 = [1,2,3,4,5,6,]


# In[83]:


final_list_new = list(map(lambda x : x*2,l1))


# In[84]:


final_list_new


# In[93]:


# lambda with reduce


# In[94]:


from functools import reduce


# In[95]:


l1 = [1,2,3,4,5,6,]


# In[100]:


sum = reduce(lambda x,y:x+y,l1)


# In[101]:


sum


# In[ ]:




