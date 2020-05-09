num1 = int(input("enter num1:", ))
num2 = int(input("enter num2:",))
Operation = input("Enter Operation:",)

if(Operation=='+'):
    print(f'sum of {num1} and {num2} is :',num1+num2)
elif(Operation=='-'):
    print(f'sub of {num1} and {num2} is :',num1-num2)
elif(Operation=='*'):
    print(f'Mul of {num1} and {num2} is :',num1*num2)
elif(Operation=='/'):
    print(f'Division of {num1} and {num2} is :',num1/num2)

