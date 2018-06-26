#Just a program to identify if a given number is prime or not
def primes(num):
    factors = 0 #counts the number of factors of the given input
    for i in range(1,num+1): #as the range function is inclusive
        if num % i == 0:
            if i == 1: #ignore the factor 1
                pass
            elif i == num: #ignore the factor if it is the given number itself
                pass
            else:
                factors += 1
        else:
            pass
    if factors == 0:
        print('Prime number') #if the number has no factors, then its prime
    else:
        print('Non-Prime number')
primes(8783479) #8783479 is just a random number to test the program. to test this program, enter any number you like
        
        
    
