def checkValidString(s):
    openStack=[]
    starStack = []
    lenght = len(s)

    for i in range(lenght):
        if s[i] == '(':
            openStack.append(i)
        elif s[i] == '*':
            starStack.append(i)
        else:
            if len(openStack) != 0:
                openStack.pop()
            elif len(starStack) != 0:
                starStack.pop()
            else:
                return False
    
    while(len(openStack)!=0):
        if len(starStack) == 0:
            return False
        elif openStack[-1] < starStack[-1]:
            openStack.pop()
            starStack.pop()
        else:
            return False
    
    return True