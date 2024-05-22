num=int (input())

def funx(num):
    summ=0
    while (num>0):
        summ=summ+num%10
        num=num//10
    # print(summ)
    if (summ>=10):
        funx(summ)
    else :
        print( summ)

funx(num)