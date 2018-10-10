######################################################################
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
######################################################################

def isPrime(x):
    for i in range(2, int(pow(x, 1/2)) + 1):
        if x % i == 0:
            return False
    return True

sum = 0
for number in range(2, 2000000):
    if isPrime(number):
        sum += number

print(sum)
# Solution: 142913828922
