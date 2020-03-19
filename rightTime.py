# -*- coding: utf-8 -*-
if __name__=="__main__":
    n = int(input())
    temp = []
    for i in range(n):
        hour,minute,second = input().split(':')
        if int(hour[0])!=0 and int(hour)>23:
            hour = ''+'0'+hour[1]
        if int(minute[0])!=0 and int(minute)>59:
            minute = ''+'0'+minute[1]
        if int(second[0])!=0 and int(second)>59:
            second = ''+'0'+second[1]
        temp.append(hour+':'+minute+':'+second)
    for mem in temp:
        print(mem)