num=int(input("Enter the num here : "))
list1=[]
sum=0
for i in range (1,num):
    if (num % i==0):
        list1.append(i)
        sum=sum+i
    else :
        continue

print(list1)
# for i in list1:
#     sum=sum+i
if (sum==num):
    print("Yes, the number is a perfect number")
else :
    print("No, the no is not a perfect number")