# -*- coding: utf-8 -*-
"""
a1 = list(map(int,input().split(',')))
a2 = list(map(int,input().split(',')))
print(a1)
print(a2)
l1,l2 = len(a1),len(a2)
newA = []
i = 0
j = 0
while i < l1 and j < l2:
    if a1[i]>=a2[j]:
        newA.append(a2[j])
        j+=1
    else:
        newA.append(a1[i])
        i+=1
print(newA)
print(i,j)
if l1>i:
    newA+=a1[i:len(a1)]
if l2>j:
    newA+=a2[j:len(a2)]
print(newA)
print(",".join(str(i) for i in newA)) 
"""
"""
a1 = list(map(int,input().split(',')))
a2 = list(map(int,input().split(',')))
print(a1)
print(a2)
"""
#要注意输入只有一行的情况，上面的缺少这个约束
a1 = list(map(int,input().split(',')))
try:
    a2 = list(map(int,input().split(',')))
    l1,l2 = len(a1),len(a2)
    i,j = 0,0
    str1 = ''
    while i < l1 and j < l2:
        if a1[i]>=a2[j]:
            str1+=str(a2[j])+','
            j+=1
        else:
            str1+=str(a1[i])+','
            i+=1
    if l1>i:
        str1+=",".join(str(i) for i in a1[i:l1])
    if l2>j:
        str1+=",".join(str(i) for i in a2[j:l2])
    print(str1)
except:
    print(",".join(str(i) for i in a1))