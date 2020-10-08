def commonCharacterCount(s1, s2):
    s = 0
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        if s1[i] in s2:
            s2.remove(s1[i])
            s = s + 1
    return s