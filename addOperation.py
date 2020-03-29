# -*- coding: utf-8 -*-
strLR = list(input().split())
str1,str2 = strLR[0],strLR[1]
n1,n2 = len(str1),len(str2)
if n1>=n2:
    str2 = '0'*(n1-n2)+str2
else:
    str1 = '0'*(n2-n1)+str1
addP,n = 0,max(n1,n2)-1
result = ''
while n>=0:
    tempV = int(str1[n])+int(str2[n])+addP
    print(tempV)
    if tempV==3 or tempV==2:
        addP = 1
        result = str(tempV%2)+result
    else:
        result = str(tempV)+result
        addP = 0
    n-=1
if addP == 1:  
    print(str(addP)+result)
else:
    print(result)