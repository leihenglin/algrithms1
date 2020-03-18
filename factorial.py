# -*- coding: utf-8 -*-
#迭代
"""
if __name__=="__main__":
    n = int(input())
    temp = 1
    for i in range(n):
        temp *= (i+1)
    print(temp)
"""

#递归
#当数目较大时，递归在空间消耗上会变大，一般不太建议
def factorial(n):
    if n <=1:
        return 1
    else:
        return n*factorial(n-1)

if __name__=="__main__":
    n = int(input())
    print(factorial(n))