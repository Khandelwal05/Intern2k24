# num=int(input("Enter the number here: "))
# flag=0
# while (num>=1):
#     if (num%2==0):
#         num=num//2
#         # flag==0
#     else :
#         flag=1
#         break
# if (flag==0):
#     print("Yes")
# else:
#     print("No")


num=int(input("Enter the number here: "))
def func(num):
    flag=0
    if (num%2==0):
        num=num/2
    else :
        flag=1
    if (flag==0 and num>0):
        func(num)
    elif (num==1):
        print("Yes")
    else :
       print("No")       
func(num)