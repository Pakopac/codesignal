def matrixElementsSum(matrix):
    s = 0
    hauntedID = []
    for row in matrix:
        for i in range(len(row)):
            if row[i] == 0:
                hauntedID.append(i)
            elif i not in hauntedID:
                s = s + row[i]
    return s