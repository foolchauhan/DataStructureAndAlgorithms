def square_digits(n):
    return sum( int(c)**2 for c in str(n) )

def isHappy(n):
    k = n
    seen = set()
    while(n != 1):
        current = n
        _sum = sum( int(c)**2 for c in str(n) )
        if _sum in seen:
            return False
        
        seen.add(_sum)
        n = _sum

    return True


print(isHappy(19))