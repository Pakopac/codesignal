def isLucky(n):
    n = str(n)
    part1 = []
    part2 = []
    for i in range(len(n)):
        if(i < len(n)/2):
            part1.append(n[i])
        else:
            part2.append(n[i])
    if sum(map(int, part1)) == sum(map(int, part2)):
        return True
    else:
        return False