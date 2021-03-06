# code that gives a list of prime factors (including repetitions) for a given number input
# tested from 1 to 10000, relatively fast in finding primes (so far)

def primecheck(n):
# code for checking if a number is prime or not
    divnum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divnum += 1 # divnum counts the factors for n
        if divnum > 2:  # if divnum > 2, there are numbers other than 1 and n that divides n
            return 1    # and so n is prime, so we choose an output of 1
            break

    if divnum == 2:
        return 0        # output of 0 if n is prime


def primefac(numorg):
# code giving the list of prime factors of a number (numorg)
    num = numorg
    plist = []
    product = 1
    for i in range(1, num + 1):
        if primecheck(i) == 0 and num % i == 0:
            plist.append(i)                       # adds i to the list of factors if it is one, and is prime
            num = int(num / i)                    
            product = product * i

            running = True
            while running:
            # this block of code tries to see if there are repeated factors, and adds them to the list
                if num % (i) == 0:
                    plist.append(i)
                    num = int(num / i)
                    product = product * i         # for each prime factor, we keep multiplying them
                    if num % (i) != 0:
                        running = False           # loop stops if the factor doesn't repeat anymore
                else:
                    running = False               # loop stops if factor doesn't divide input number

        if product == numorg:
        # once product is equal to our input number, we stop the for loop, since we've found all the prime factors by then
            break
            
    return plist
    # returns our list of prime factors of the input number early on
