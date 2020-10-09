def arrayChange(inputArray):
    sum = 0
    for i in range(len(inputArray)):
        if i != len(inputArray) - 1:
            if (inputArray[i+1] <= inputArray[i]):
                while inputArray[i+1] <= inputArray[i]:
                    inputArray[i+1] = inputArray[i+1] + 1
                    sum = sum + 1
    return sum