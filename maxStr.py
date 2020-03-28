# -*- coding: utf-8 -*-
strs = input().replace("[","").replace("]","").replace('"',"").split(",")
maxLen = 0   
""" 
maxLen = 0
for i in range(len(strs)-1):
    tempStrs = strs[i+1:len(strs)]
    for j in tempStrs:
        flag=0
        for c in strs[i]:
            if c in j:
                flag=1
                break
        if flag==0:
            if maxLen<len(strs[i])*len(j):
                print(strs[i],j)
                maxLen = len(strs[i])*len(j)
print(maxLen)
"""

for i in range(len(strs)-1):
    tempStrs = strs[i+1:len(strs)]
    for str2 in tempStrs:
        s1,s2 = set(strs[i]),set(str2)
        if len(s1)+len(s2)==len(s1|s2) and maxLen<len(s1)*len(s2):
                maxLen = len(s1)*len(s2)
print(maxLen)
