# -*- coding: utf-8 -*-
n = 3
P = [1,2,3]
def Perm1(m):
    if m==n:
        print(P)
    else:
        for j in range(m,n):  
            P[j],P[m] = P[m],P[j]
            Perm1(m+1)
            P[j],P[m] = P[m],P[j]
def generationPerm():
    Perm1(0)
if __name__ == "__main__":
    generationPerm()