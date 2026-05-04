num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
operation = input ("choose your operayion + - * / : ")
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1/num2)
else:
    print("please put a valid operation amongst the ones listed above")