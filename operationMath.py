if __name__=="__main__":
    i=0
    sum1 = 0
    s = input()
    n = len(s)
    #对于第一个字符是数字的情况，在它前面添加一个+号，统一为一种类型的输入
    if s[0] != '+' and s[0] != '-':
        s = '+'+s
        n+=1
    while i < n-1:
        j = i+1
        if s[i]=='+' or s[i]=='-':
            while j<n:
                if s[j] != '+' and s[j] != '-':
                    j+=1
                else:
                    break
            if s[i]=='+':
                sum1+=int(s[i+1:j])
            else:
                sum1-=int(s[i+1:j])
        i=j
    print(sum1)