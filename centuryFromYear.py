def centuryFromYear(year):
    if str(year/100-int(year/100))[1:] == ".0":
        return math.floor(year/100)
    elif len(str(year)) != 4:
        return math.ceil(year/100)
    else:
        return math.floor(year/100) + 1
