lst1=list(input("Enter the list here: "))
lst2=[]
for i in lst1:
    if i in lst2:
        continue
    else :
        lst2.append(i)
print(lst2)