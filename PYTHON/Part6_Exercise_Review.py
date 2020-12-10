#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:-2])
# 'jan'
print(s[1:4])
# 'go'
print(s[-2:])
# Bonus: Use indexing to reverse the string
print(s[::-1])

###############
## Problem 2 ##
###############
print('---------------------------------')
# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
#print(l)
l[2][2] = 'goodbye'
print(l)
###############
## Problem 3 ##
###############
print('-----------------------------------')
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
###############
## Problem 4 ##
###############
print('-------------------------------------')
# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

###############
## Problem 5 ##
###############
print('--------------------------------------')
# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {a} and he is {b} years old".format(a=name,b=age))