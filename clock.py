# -*- coding: utf-8 -*-
if __name__=="__main__":
    minc = lambda m,n:m*60+n
    n = int(input())
    times=[minc(*list(map(int, input().split()))) for i in range(n)]
    
    toClassroom = int(input())
    endTime = list(map(int,input().split()))
    endTime = endTime[0]*60+endTime[1]
    lastTime = endTime - toClassroom
    maxTemp = 0
    for i in times:
        if i <= lastTime:
            if i>=maxTemp:
                maxTemp = i

    print(maxTemp//60,maxTemp%60)
            