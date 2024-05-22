N=int (input("Enter the number of terms here: "))
arr=[]
k=int(input("Enter the value of k here "))
for i in range (N):
    a=int(input("Enter the elements of array "))
    arr.append(a)

print(arr)
count=0
for i in range(N):
    for j in range(i+1, N):
        if (arr[i]+arr[j]==k):
            count=count+1
        else:
            continue
print(count)