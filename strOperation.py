# -*- coding: utf-8 -*-
"""
numbs=list(map(int,input().split()))
N,T = numbs[0],numbs[1]
strOrigin = input()
while T>0:
    operation=list(map(int,input().split()))
    TYPE,loc = operation[0],operation[1]
    if TYPE==1:
        strOrigin = ''+strOrigin[N-loc:N]+strOrigin[0:N-loc]
    elif TYPE==2:
        print(strOrigin[loc])
    T-=1
"""
N,T=[int(x) for x in input().split()]
strOrigin = input()
for i in range(T):
    TYPE,loc=[int(x) for x in input().split()]
    if TYPE==1:
        strOrigin = ''+strOrigin[N-loc:N]+strOrigin[0:N-loc]
    elif TYPE==2:
        print(strOrigin[loc])