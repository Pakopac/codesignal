def adjacentElementsProduct(inputArray):
    tab = []
    for i in range(len(inputArray)):
        if len(inputArray) != i + 1:
            tab.append(inputArray[i] * inputArray[i + 1])

    max = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
    return max


