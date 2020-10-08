def reverseInParentheses(inputString):
    letters = []
    for i in range(len(inputString)):
        if(inputString[i] == '('):
            j = i
            start = j+1
            while inputString[j+1] != ')':
                letters.append(inputString[j+1])
                j = j + 1
            if '(' in letters:
                inputString2 = inputString.replace(''.join(letters),','.join(','.join(letters).split('(')[1]).replace(',','') + 
                ','.join(','.join(letters).split('(')[0])[::-1].replace(',',''))
                inputString2 = inputString2.replace('(','')
                inputString2 = inputString2.replace(')','')
                return inputString2
            else:               
                inputString = inputString.replace(''.join(letters), ''.join(letters[::-1]))
            letters = []
            
    inputString = inputString.replace('(','')
    inputString = inputString.replace(')','')
    return inputString