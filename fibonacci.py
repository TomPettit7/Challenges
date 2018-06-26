def fibonacci(limit): #enter a number that is half of the desired range
    a = 1 #first terms of the fibonacci sequence
    b = 1

    for i in range(1, limit+1): #range isn't inclusive on upper limit
        a+=b
        b+=a #modelling the fibonacci sequence
        print(a)
        print(b)

fibonacci(5) #testing the code with a range of 10 numbers
