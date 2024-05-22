N=int (input("Enter the number of terms here: "))
arr=[]
d=int(input("Enter the value of d here "))
for i in range (N):
    a=int(input("Enter the elements of array "))
    arr.append(a)
print(arr)

def rotate(arr, d):
    return arr[-d:]+ arr[:-d]

r=rotate(arr, d)
print(r)