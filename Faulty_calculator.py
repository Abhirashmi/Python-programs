op = input("Enter the operator which you want to use(+,-,*,/):")
num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2st Number:"))
if op == "+":
    if num1 == 56 or num1 == 9:
        if num2 == 9 or num2 == 56:
            print("Addition of", num1, " and", num2, " is 77")
    else:
        print("Addition of",num1," and",num2," is ",num1+num2)
elif op == "*":
    if num1 == 45 or num1 == 3:
        if num2 == 3 or num2 == 45:
            print("Multiplication of", num1, " and", num2, " is 555")
    else:
        print("Multiplication of",num1," and",num2," is ",num1*num2)
elif op == "/":
    if num1 == 56 and num2 == 6:
        print("Multiplication of", num1, " and", num2, " is 4")
    else:
        print("Division of", num1, " and", num2, " is ", num1 / num2)
elif op == "-":
    print("Subtraction of", num1, " and", num2, " is ", num1 - num2)
else:
    print("Enter valid Operator")