print("**************EXAMPLE!********************")
def my_function(str1,str2):
    print(str1)
    print(str2)
my_function("First string","Second string")
my_function("Hello","World")

print("**************EXAMPLE2******************")
def new_func(name,age):
    print("My name is "+ name + "and my age is " + str(age) )
    print("My name is ", name, "and my age is ",age)
new_func("AKB",26)

print("**************INFINITE ARGUMENT******************")
def print_pple(*people):
    for person in people:
        print("This person is",person)
print_pple("Nick","Jonas","Kim","John")

print("***********RETURN****************")
def do_math(num1,num2):
    return num1+num2
math1= do_math(5,7)
math2= do_math(2,3)
print ("first sum is ",math1," and second sum is ",math2)