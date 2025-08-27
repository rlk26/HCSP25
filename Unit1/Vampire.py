def is_vampire(x, awake):
    if ((x > 22 or x < 6) and awake == True):
        return True
    elif (x < 22 and x > 6 and awake == False):
        return True
    else:
        return False
    
def is_vampireTest(x, awake, expected):
    correct = is_vampire(x, awake)
    if (correct == expected):
        return True
    else:
        return False


print (is_vampireTest(3, False, False))
print (is_vampireTest(3, True, True))
print (is_vampireTest(8, True, False))
print (is_vampireTest(23, True, True))