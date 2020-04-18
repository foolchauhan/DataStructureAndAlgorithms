def stringShift(s, shift):
    leftShift = rightShift = 0
    shifts = 0
    lengthS = len(s)
    for lst in shift:
        if lst[0] == 0:
            leftShift += lst[1]
        elif lst[0] == 1:
            rightShift += lst[1]
    
    if leftShift == rightShift:
        return s
    elif leftShift > rightShift:
        shifts = (leftShift - rightShift)%lengthS
        return s[shifts:]+s[:shifts]
    elif rightShift > leftShift:
        shifts = (rightShift-leftShift)%lengthS
        return s[lengthS-shifts:] + s[:lengthS-shifts]

print(stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))