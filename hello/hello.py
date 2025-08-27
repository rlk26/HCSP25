for i in range (1, 31):
    if i%3 == 0:
        print (i)
        
for i in range (1, 31):
    if i%3 == 0 and i%5 == 0:
        print ("FizzBuzz")
    elif i%3 == 0:
        print ("Fizz")
    elif i%5 == 0:
        print ("Buzz")
    else:
        print(i)

value = 3
for i in range (10):
    print(value)
    value *= 2
    

for i in range (10):
    print(i * i * i)
  

a = 0
b = 1
for i in range (-1, 10):
    if i == 0:
        print(a+b)
        a = a+b
    if i%2 ==0:
        print(a+b)
        a = a+b
    else:
        print (a+b)
        b = a+b
