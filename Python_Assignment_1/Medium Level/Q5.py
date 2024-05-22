N=int (input("Enter the number of terms here: "))
arr=[]
for i in range (N):
    a=int(input("Enter the elements of array "))
    arr.append(a)
sum=0
for i in arr:
    sum=sum+i
avg=sum/N
print("Average temp is ", avg)
print("Highest temp is ", max(arr))
print ("Lowest temp is ", min(arr))