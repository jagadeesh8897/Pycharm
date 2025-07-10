def sumAndAverage(li):
    print(sum(li))
    print(sum(li)//len(li))
    return li[::-1]
lis=list(map(int,input("Enter 5 numbers :").split()))
print(sumAndAverage(lis))
