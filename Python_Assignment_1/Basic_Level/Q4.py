a=int(input("Enter the starting number here"))
b=int(input("Enter the ending number here"))
sum=0
for i in range (a, b+1):
    if (i%2!=0):
        sum=sum+i
print("Sum of all odd numbers between ",a ," and ",b, "is :",sum)