# -*- coding: utf-8 -*-
n = int(input())
numbs = list(map(int,input().split()))
counts = 0
i = 0
while len(numbs)>0:
    firstNum = numbs[0]
    del numbs[0]
    indexElse = numbs.index(firstNum)
    counts+=indexElse
    del numbs[indexElse]
print(counts)
