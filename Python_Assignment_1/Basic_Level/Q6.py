string1=input("Enter the string 1 here")
string2 =input("Enter the string 2 here")
flag=0
for i in string1:
    if (i in string2):
        string2.replace(i, '0')
    else :
        flag=1
        break
if (flag==0):
    print("Yes")
else :
    print("No")