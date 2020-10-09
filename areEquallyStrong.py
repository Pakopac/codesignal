def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft > yourRight:
        if friendsLeft > friendsRight:
            if yourLeft == friendsLeft and yourRight == friendsRight:
                return True
            else:
                return False
        else:
            if yourLeft == friendsRight and yourRight == friendsLeft:
                return True
            else:
                return False
    else:
        if friendsLeft > friendsRight:
            if yourRight == friendsLeft and yourLeft == friendsRight:
                return True
            else:
                return False
        else:
            if yourRight == friendsRight and yourLeft == friendsLeft:
                return True
            else:
                return False