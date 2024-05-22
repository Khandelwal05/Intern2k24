list1=['Red','Blue','Pink']
def func(l):
    list2=[]
    for ele in l:
        list2.append(ele)
    return list2

result=map(func, list1)
print(list(result))

