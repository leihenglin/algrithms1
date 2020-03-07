# -*- coding: utf-8 -*-
#比如输入CCCCDCDC 试着将其分开，结果为CCCCCCDD
if __name__=="__main__":
    count1 = 0
    count2 = 0
    str1 = input()
    n = len(str1)
    #计算所有C往右移的次数和所有D往右移次数，取二者中较小值
    for i in range(n):
        if str1[i] == 'D':
            j1 = i+1
            while j1<n:
                if str1[j1]=='C':
                    count1 +=1
                j1+=1
        else:
            j2 = i+1
            while j2<n:
                if str1[j2]=='D':
                    count2 +=1
                j2+=1
    print(min(count1,count2))