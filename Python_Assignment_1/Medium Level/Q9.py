try:
    list1=[1,2,3,4,5]
    list1.append(6)
    list1.remove(2)
    print(list1)
    list1[8]
except IndexError as e:
    print("Error",e)