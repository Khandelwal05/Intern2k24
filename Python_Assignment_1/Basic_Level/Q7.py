num1=int(input("Enter the num1 here: "))
num2=int(input("Enter the second no here : "))
list1=[]
list2=[]
for i in range (1,num1+1):
    if (num1%i==0):
        list1.append(i)
    else :
        continue
for j in range (1,num2+1):
    if (num2%j==0):
        list2.append(j)
    else :
        continue

lcm=1
for i in list1:
    if i in list2:
        lcm=lcm*i
    else :
        continue

print("LCM is ", lcm)