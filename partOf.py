# -*- coding: utf-8 -*-
"""
#第一种方法，使用简便方法
if __name__=="__main__":
    while True:
        try:
            str1 = input().split()
            pre = str1[0]
            tail = str1[1]
            
            if pre in tail or tail in pre:
                print(1)
            else:
                print(0)
        except:
            break
"""

if __name__=="__main__":
    while True:
        try:
            flag = 0
            str1 = input().split()
            pre,tail = str1[0],str1[1]
            len1,len2 = len(pre),len(tail)

            if len1>=len2:
                i = 0
                while i < len1:
                    if pre[i:i+len2]==tail:
                        flag = 1
                        break
                    i+=1
            else:
                j = 0
                while j < len2:
                    if tail[j:j+len1]==pre:
                        flag = 1
                        break
                    j+=1
            
            print(1 if flag == 1 else 0)
        except:
            break