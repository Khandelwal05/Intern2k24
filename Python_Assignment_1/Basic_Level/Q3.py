
a=[]
list1=['Maths', 'Physics', 'Chemistry', 'Computer', 'Biology']
for i in list1 :
    print("Enter the marks of ", i)
    a.append(int(input()))
print(a)
sum=0
for i in a :
    sum=sum+ i
percentage=sum/5

if (percentage>=90):
    print("Grade : A" )
elif (percentage>=80):
    print("Grade : B" )
elif (percentage>=70):
    print("Grade : C" )
elif (percentage>=60):
    print("Grade : D" )
elif (percentage>=40):
    print("Grade : E" )
elif (percentage>=0 and percentage<40):
    print("Grade : F" )
else : 
    print("Enter valid marks")