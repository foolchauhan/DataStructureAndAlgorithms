def backspaceCompare(S: str, T: str):
    S_final = ''
    for i in range(len(S)):
        if S[i] != '#':
            S_final = S_final + S[i]
        else:
            if(len(S_final) > 0):
                S_final = S_final[:-1]

    T_final = ''
    for i in range(len(T)):
        if T[i] != '#':
            T_final = T_final + T[i]
        else:
            if(len(T_final) > 0):
                T_final = T_final[:-1]

    return S_final==T_final

print(backspaceCompare("ab#c", "ad#c"))
    

