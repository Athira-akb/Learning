import  re
str="I do not yell!, she said. Though we knew it was not true."
print(re.sub('[A-Z+" "]','',str))
print (re.sub('[a-z]','*',str))
print (re.sub('[A-Z]',' ',str))