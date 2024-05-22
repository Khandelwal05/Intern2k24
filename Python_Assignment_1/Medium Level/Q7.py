N=int (input("Enter the number of terms here: "))
arr=[]
for i in range (N):
    a=int(input("Enter the elements of array "))
    arr.append(a)

arr.sort()
print(arr)

if (N%2==0):
    i=(N//2)-1
    med=(arr[i]+arr[i+1])/2
else :
    i=(N//2)+1
    med=arr[i]/2
print(med)