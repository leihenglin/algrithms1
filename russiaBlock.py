# -*- coding: utf-8 -*-
if __name__=="__main__":
    mn = list(map(int,input().split()))
    n,m = mn[0],mn[1]
    column = [0 for i in range(n)]
    blocks = list(map(int,input().split()))
    for i in range(m):
        column[blocks[i]-1]+=1
    print(min(column))
        