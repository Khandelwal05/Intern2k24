user=input("Entre the string here :")
alpha=0
nums=0
user=user.upper()

for char in user:
    if 'A' <=char <='Z':
        alpha+=1
    elif '0'<=char<='9':
        nums+=1
print("Apha -> ", alpha)
print("nums -> ", nums)

