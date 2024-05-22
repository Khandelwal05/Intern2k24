import math
num1=int(input("Enter the num1 here: "))
num2=int(input("Enter the second no here : "))

a=math.gcd(num1, num2)

lcm=(num1*num2)//a
print(lcm)