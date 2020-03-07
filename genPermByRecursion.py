# -*- coding: utf-8 -*-
import sys
def Perm1(s,k,n,count):
    s1=''
    i,j = n,n
    print(s)
    #递归出口
    if k==count: sys.exit()
    #从左向右找到第一个左边值比右边值小的数的位置
    while i>=2:
        if int(s[i-2])<int(s[i-1]):
            minIndex = i-2
            break
        i-=1
    #从左向右找到第一个比上步位置值大的数的位置
    while j>0:
        if int(s[minIndex])<int(s[j-1]):
            maxIndex = j-1
            break
        j-=1
    #交换上边两个位置的值
    s1 = s[0:minIndex]+s[maxIndex]+s[minIndex+1:maxIndex]+s[minIndex]+s[maxIndex+1:n]
    #对于交换后的str，逆序第一个位置后的值
    s2 = s1[0:minIndex+1]+s1[-1:-(n-minIndex):-1]
    Perm1(s2,k+1,n,count)

def generationPerm():
    s = '1234'
    n=len(s)
    count = 1
    for i in range(n):
        count*=(i+1)
    Perm1(s,1,n,count)

if __name__=="__main__":
    generationPerm()