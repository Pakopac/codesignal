def sortByHeight(a):
    treesID = []
    for i in range(len(a)):
        if a[i] == -1:
            treesID.append(i)
    a = list(filter(deleteTrees, a))
    a = sorted(a)
    for i in range(len(treesID)):
        print(treesID[i])
        a[treesID[i]: treesID[i]] = [-1]
    return a    
    
def deleteTrees(a):
    if(a != -1):
        return True
    else:
        return False