def addBorder(picture):
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    asterisksRow = ""
    for i in range(len(picture[0])):
        asterisksRow = asterisksRow + "*"
    picture.insert(0, asterisksRow)
    picture.insert(len(picture),asterisksRow)
    return picture