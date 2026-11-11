#text based calculator project using python
num_1 = (input("Number1: "))
num_2 = (input("Number2: "))
sign = input("Sign: ")
#variable = input("please enter the number : ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    
except:
    print("Invalid operation !")
if (sign == "+"):
    print(num_1 + num_2)
    
elif (sign == "-"):
    print(num_1 - num_2)
    
elif (sign == "/"):
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Divided by zero")
    
elif (sign == "*"):
    print(num_1 * num_2)
    
else :
    print(num_1 % num_2)