# -*- coding: utf-8 -*-
str1,str2 = input().split()
flag = 0
for k in str1:
    if k in str2:
        str2=str2.replace(k,'',1)
    else:
        flag = 1
        break
print('false' if flag==1 else 'true')
