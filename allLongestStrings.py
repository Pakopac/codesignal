def allLongestStrings(inputArray):
    longestStrings = [""]
    for i in range(len(inputArray)):
        if len(inputArray[i]) == len(longestStrings[0]):
            longestStrings.append(inputArray[i])
        elif len(inputArray[i]) > len(longestStrings[0]):
            longestStrings = [inputArray[i]]
    return longestStrings