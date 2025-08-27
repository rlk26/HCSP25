def is_prime(n):
    for i in range(2, 101):
        if (i%n != 0 and i != 1):
            print(i)
        else 
            print(FALSE)
    
def is_primeTest(n, expected):
    correct = is_prime(n)
    if (correct == expected):
        return True
    else:
        return False

print (is_prime(3))
print (is_prime(5))
print (is_prime(7))