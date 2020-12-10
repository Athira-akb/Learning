import re
run = True
previous = 0
print("***************CALCULATOR (+,-,*,/)*************")
print("Type 'quit' to exit!")
print("Write anything within quotations('') \n")

def math_calc():
    global run
    global previous
    equation = ""

    #Previous = 0 means 1st time using calculator
    if previous == 0:
        equation = input("Enter equation :")

    #when the output of 1st equation is treated as input so that
    # further calculation can be done with result
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Goodbye Human!!")
        run = False

    else:
        equation= re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous==0:
            previous= eval(equation)
        else :
            previous=eval(str(previous)+equation)
        print ("Result is : ",previous)

while run:
    math_calc()