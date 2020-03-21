"""
直接字符串拼接,时间开销太大
if __name__=="__main__":
    numbs = list(map(int,input().split()))
    result = []
    s = ''
    for v in numbs:
        if v&1==0:
            s = str(v)+' '+s
            #result.insert(0,v)
        else:
            s = s+' '+str(v)
            #result.append(v)
    #print(result)
    print(s)
"""
"""
交换方法，时间复杂度超过O（2n），能在规定时间允许
1 3 4 5 6 7
4 3 1 5 6 7

if __name__=="__main__":
    numbs = list(map(int,input().split()))
    result = []
    j = 0
    s = ''
    for i in range(len(numbs)):
        if numbs[i]&1==0:
            temp = numbs[j]
            numbs[j] = numbs[i]
            numbs[i] = temp
            j+=1
            
    print(numbs)
    for v1 in numbs:
        s+=str(v1)+' '
    print(s.strip())
"""

if __name__=="__main__":
    j = 0
    numbs = list(map(int,input().split()))
    for i in range(len(numbs)):
        if numbs[i]&1==0:
            numbs[j],numbs[i] = numbs[i],numbs[j]
            j+=1
    print(' '.join(map(str, numbs)))