"""
# -*- coding: utf-8 -*-
if __name__=="__main__":
    j = 0
    flag = 0
    n = int(input())
    numbs  = list(map(int,input().split()))
    numbs.sort()
    #print(numbs)
    while j<n-1:
        if numbs[j]!=numbs[j+1]:
            flag = 1
            print(numbs[j])
            break
        j+=2
    if flag == 0:
        print(numbs[n-1])
"""
"""
#空间换时间，字典
if __name__=="__main__":
    numDic = {}
    n = int(input())
    numbs  = list(map(int,input().split()))
    for i in numbs:
        if i in list(numDic.keys()):
            numDic[i]=2
        else:
            numDic[i] = 1
    k = list(numDic.keys())
    v = list(numDic.values())
    print(k[v.index(1)])
"""

#最终版，异或操作，相同为0，任何数和0异或为它本身
n = int(input())
res = list(map(int, input().split()))
num = 0
for i in res:
    num = num^i
print(num)