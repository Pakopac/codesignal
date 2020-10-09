def areSimilar(a, b):
    idArray = []
    values = []
    for i in range(len(a)):
        if a[i] != b[i]:
            idArray.append(i)
            values.append(a[i])
    if len(values) < 3:
        values = values[::-1]
        for i in range(len(values)):
            a[idArray[i]] = values[i]
        if a == b:
            return True
        else:
            return False
    else:
        return False