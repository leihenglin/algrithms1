# -*- coding: utf-8 -*-
gs = sorted(list(map(int,input().split())))
ss = sorted(list(map(int,input().split())))
i,j,counts = 0,0,0
while j<len(ss) and i<len(gs):
    if ss[j]>=gs[i]:
        i+=1
        j+=1
        counts+=1
    else:
        j+=1
print(counts)