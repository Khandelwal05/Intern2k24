num=int(input("Enter the number here"))
if (num%3==0):
    print("Brudite")
elif (num%5==0):
    print("Python Training")
elif (num%3 ==0 and num %5==0 ):
    print("Brudite - Python Training")
else :
    print("No is not divisible by 3 or 5 ")