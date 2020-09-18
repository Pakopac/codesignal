def checkPalindrome(inputString):
    tab1 = []
    tab2 = []
    if (len(inputString) % 2) == 0:
        for i in range(len(inputString)):
            if i < len(inputString) / 2:
                tab1.append(inputString[i])
            else:
                tab2.insert(0, inputString[i])
    else:
        for i in range(len(inputString)):
            if i < len(inputString) / 2 - 1:
                tab1.append(inputString[i])
            elif i > len(inputString) / 2:
                tab2.insert(0, inputString[i])

    if tab1 == tab2:
        return True
    else:
        return False

