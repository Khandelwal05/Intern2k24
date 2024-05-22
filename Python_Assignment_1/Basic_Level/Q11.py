num=int(input("Enter the number here: "))
num2=0
while (num>0):
    num2=num2*10+num%10
    num=num//10

print(num2)
