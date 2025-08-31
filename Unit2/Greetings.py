def greetings(n):
    return ("Hello," + n + ", how are you?")
    
def greetingsTest(n, expected):
    correct = greetings(n)
    if (correct == expected):
        return True
    else:
        return False
    
print(greetingsTest("Nina",  "Hello," + "Nina" + ", how are you?"))
print(greetingsTest("Sarah",  "Hello," + "Sarah" + ", how are you?"))
print(greetingsTest("Briley",  "Hello," + "Briley" + ", how are you?"))