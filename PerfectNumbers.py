import time
firstlapsestart = time.time()

#write an algorithm that finds perfect numbers the slow way
def divlist(x):
    thelist = [i for i in range(1,x) if x%i == 0]
    return thelist
def perfectnumbersI(x):
    perfectnumbers = list()
    for i in range(1,x):
        divisorsum = 0
        for e in divlist(i):
            divisorsum += e
        if divisorsum == i:
            perfectnumbers.append(i)
    return perfectnumbers

print(perfectnumbersI(100000))
firstlapseend = time.time()
#a better formula a la Euclid-Euler
#first need to define what a prime number is
def isprime(x):
    if x>1:
        if len(divlist(x)) == 1:
            return True
        else:
            return False
    else:
        return False

def primegenerator(n): #gives all primes between 1 and n
    return [p for p in range(n) if isprime(p) == True]
#print(primegenerator(100))

secondlapsestart = time.time()

def perfectnumbersII(x):
    perfectnumbers = list()
    #get the first x perfect numbers by using the first x prime numbers
    for i in primegenerator(100)[0:x]: #don't really need primes bigger than 100, but can replace the number if wanting to go bigger
        p = ((2**i)-1) * (2**(i-1))
        perfectnumbers.append(p)
    return perfectnumbers

print(perfectnumbersII(10))
secondlapseend = time.time()

print("Amount of time spent calculating Perfect Numbers the slow way: {} seconds".format((firstlapseend - firstlapsestart)))
print("Amount of time spent calculating Perfect Numbers using Euler-Euclid method: {} seconds".format((secondlapseend - secondlapsestart))) 


