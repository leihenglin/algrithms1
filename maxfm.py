# -*- coding: utf-8 -*-
"""
def getZS(m):
    list1 = set()
    for k in range(2,m+1):
        while k != m:
            if m%k==0:
                list1.add(k)
                m=m//k
            else:
                break
    list1.add(m)
    return list1

if __name__=="__main__":
    n = int(input())
    numbs =list(map(int,input().split()))  
    sets1 = set()  
    for k in numbs:
        sets1 = sets1|getZS(k)
    print(sets1)
    j = 1
    while True:
        flag = 0
        for i in sets1:
            if j%i != i-1 or j<:
                flag = 1
        if flag == 0:
            print(j)
            break
        j+=1
"""
#重点在找规律
if __name__=="__main__":
    n = int(input())
    numbs =list(map(int,input().split()))  
    print(sum(numbs)-n)