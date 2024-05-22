list1=list(input("Enter the list here"))
print("List is ", list1)
dict1={}
count=0
for i in list1:
    if (i not in dict1.keys()):
        dict1[i]=list1.count(i)
print(dict1)
    