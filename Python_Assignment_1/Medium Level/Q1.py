lst1=list(input("Enter list 1 here: "))
lst2=list(input("Enter list 2 here: "))
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
    else : 
        continue
print(lst3)
    