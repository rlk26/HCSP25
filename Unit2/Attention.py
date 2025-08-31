def attention(n):
    if (n[0:8] == "Hey you!"):
        return True
    else:
        return False
    
def attentionTest(n, expected):
    correct = attention(n)
    if (correct == expected):
        return True
    else:
        return False
    
print(attentionTest("Hey you! I'm ramya", True))
print(attentionTest("hiiiiiii ninnaaaaaaa", False))
print(attentionTest("this thing is dumb", False))
