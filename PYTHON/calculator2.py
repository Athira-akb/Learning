print("CALCULATION PROGRAMME")
print("Different operators are ")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("quit = To exit")

def calc_add(num1,num2):
    return num1 + num2
def calc_sub(num1,num2):
    return num1 - num2
def calc_mul(num1,num2):
    return num1*num2
def calc_div(num1,num2):
    return num1/num2

run = True

def calc_fn():
    global run
    inp = ""
    inp = input("Enter the desiered operator (1/2/3/4/quit) :")
    if inp == "quit":
        run = False
        print ("Exiting calculator")
    else:
        n1 = input("Enter the first number : ")
        n2 = input("Enter the second number : ")
        if inp == 1:
            print ("Sum is :", calc_add(n1, n2))
        elif inp == 2:
            print("Difference is : ", calc_sub(n1, n2))
        elif inp == 3:
            print("Product is : ", calc_mul(n1, n2))
        elif inp == 4:
            print("Quotient is : ", calc_div(n1, n2))
        else:
            print("Invalid operator!")
while run:
    calc_fn()



'''if cont == "No":
    run = False
    print("Exiting...")
else:
    print("Let us continue!!")'''