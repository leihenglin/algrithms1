# -*- coding: utf-8 -*-
"""
if __name__=="__main__":
    n = int(input())
    appleHeap = list(map(int,input().split()))
    temp = 0
    countAdd = []
    for i in appleHeap:
        temp+=i
        countAdd.append(temp)
    
    queryTimes = int(input())
    querys = list(map(int,input().split()))
    for q in querys:
        for i in range(n):
            if countAdd[i] >= q:
                print(i+1)
                break
"""

if __name__=="__main__":
    n = int(input())
    appleHeap = list(map(int,input().split()))
    temp = 0
    countAdd = []
    for i in appleHeap:
        temp+=i
        countAdd.append(temp)
    
    queryTimes = int(input())
    querys = list(map(int,input().split()))
    for q in querys:
        left = 0
        right = n-1
        print(q)
        print("/")
        while left <= right:
            
            mid = (left+right)//2
            print(mid)
            if mid == 0:
                print(mid+1)
                break
            if mid == n-1:
                print(mid+1)
                break
            else:
                
                if countAdd[mid-1]>q and countAdd[mid]>q and countAdd[mid+1]>q and mid+1<n:
                    right = mid-1
                    print("&")
                elif countAdd[mid]<q:
                    left = mid + 1
                    print("*")
                elif countAdd[mid]>q and countAdd[mid-1]<q and mid-1>=0:
                    print(mid)
                    print("#")
                    break