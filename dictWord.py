# -*- coding: utf-8 -*-
import sys
if __name__=="__main__":
    input1 = list(map(int,input().split()))
    n,m,k = input1[0],input1[1],input1[2]
    s = ''
    for i in range(n+m):
        if i<n:
            s+='a'
        else:
            s+='z'
    kt=1
    n = len(s)
    while(kt<=k):
        if kt==k:
            print(s)
            sys.exit()
        l1 = n-1
        l2 = n-1
        left = 0
        right = 0
        while l1>0:
            if s[l1-1]<s[l1]:
                left = l1-1
                break
            l1-=1
        while l2>0:
            if s[left]<s[l2]:
                right = l2
                break
            l2-=1
        temp_s = s[0:left]+s[right]+s[left+1:right]+s[left]+s[right+1:n]
        temp1_s = temp_s[0:left+1]
        temp1_s+=temp_s[left+1:n][::-1]
        s = temp1_s
        kt+=1