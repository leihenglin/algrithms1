# -*- coding: utf-8 -*-
if __name__=="__main__":
    n = int(input())
    numbs = list(map(int,input().split()))
    maxValue = 0
    l=0
    r=n-1
    s1,s2= numbs[0],numbs[r]
    while l<r:
        if s1<s2:
            s1+=numbs[l+1]
            l+=1
        elif s1>s2:
            s2+=numbs[r-1]
            r-=1
        else:
            if s1>maxValue:
                maxValue = s1
                s1+=numbs[l+1]
                s2+=numbs[r-1]
                l+=1
                r-=1
    print(maxValue)