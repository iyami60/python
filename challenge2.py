def verifierNum(strin):
    numeros  = "1234567890-."
    for i in range(len(strin)):
        if strin[i] in numeros:
            continue
        else:
            return 0
    return 1
            
#print(verifierNum("12c53"))

def rever(string):
    if verifierNum(string) == 1:
        k = len(string)-1
        result = 0
        num = int(string)
        if num<0:
            abso = num*(-1)
            sign = -1
            k = k-1
        else:
            abso = num
            sign = 1
        for i in range(len(string)-1):
            a = abso % 10
            result = result+a*(10**k)
            abso = abso//10
            k = k-1
        result = result + abso
        return result*sign
    else : 
        return "entrer Un nombre valide"

print(rever("-45123"))