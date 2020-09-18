def makeArrayConsecutive2(statues):
    statues.sort()
    s = 0
    for i in range(len(statues)):
        print(i, statues[i] - statues[i - 1])
        if statues[i] - statues[i - 1] > 1:
            s = s + statues[i] - statues[i - 1] - 1
    return s