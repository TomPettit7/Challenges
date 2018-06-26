#This prints all the factors of a given number

def divisors(integer):
    factors = 0 #counts the number of factors the number has

    if integer > 1:
        for num in range(1,integer+1): #integer+1 as the range isn't inclusive on the larger side
            if integer % num == 0:
                if num == 1:
                    pass  #ignore the factor 1
                elif num == integer: #ignore the factor which is the given number
                    pass
                else:
                    print(num)
                    factors += 1
    if factors == 0:
        print(str(integer)+' is a prime') #if the number inputed has no factorsl, then it must be prime


    

