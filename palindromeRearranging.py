def palindromeRearranging(inputString):
    countChar = {i:inputString.count(i) for i in inputString}
    even = 0
    for i in countChar:
        if (len(inputString) % 2) == 0:
            if (countChar[i] % 2) != 0:
                return False
        else:
            if (countChar[i] % 2) != 0:
                if even == 0:
                    even = even + 1
                else:
                    return False
            
    return True