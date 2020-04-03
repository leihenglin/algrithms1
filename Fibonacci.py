# -*- coding: utf-8 -*-
"""
动态规划自底向上，速度相比递归快很多
def f(n):
    d = [0]*n
    d[0]=1
    d[1]=2
    for i in range(2,n):
        d[i] = d[i-1]+d[i-2]
    
    return d[-1]


if __name__=="__main__":
    n = int(input())
    print(f(n))
"""

"""
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return f(n-1)+f(n-2)

if __name__=="__main__":
    n = int(input())
    print(f(n))
"""