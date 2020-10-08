def almostIncreasingSequence(sequence):
    for i in range(len(sequence)):
        if i != 0:
            if sequence[i] <= sequence[i-1]:
                if i != len(sequence) - 1 and sequence[i+1] <= sequence[i-1]:
                    del sequence[i-1]
                    return checkSequence(sequence)
                else:
                    del sequence[i]
                    return checkSequence(sequence)
    return True
    
def checkSequence(sequence):
    for j in range(len(sequence)):
        if j != 0:
            if sequence[j] <= sequence[j-1]:
                print(sequence[j])
                return False
    return True