if __name__=="__main__":
    s = input()
    flag = 0
    brackets = []
    flag == 0
    for i in s:
        if i=='[' or i =='(':
            brackets.append(i)
        elif i==']':
            if not brackets or brackets.pop()!='[':
                flag=1
                break
        
        elif i==')':
            if not brackets or brackets.pop()!='(':
                flag=1
                break
        else:
            pass
    if brackets:
        flag=1
    print('false' if flag == 1  else 'true')