str1=input("Enter the string here: ")
count=0
str1=str1.lower()
print(str1)
for i in str1:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
    else :
        continue
print(count)