def good_deal(originalPrice, salePrice):
    if (originalPrice*.75 > salePrice):
        return True
    else:
        return False
    
def is_good_deal(originalPrice, salePrice, expected):
    correct = good_deal(originalPrice, salePrice)
    if (correct == expected):
        return True
    else:
        return False


print (is_good_deal(5, 10, False))
print (is_good_deal(100, 60, True))
print (is_good_deal(20, 30, False))
print (is_good_deal(10, 2, True))