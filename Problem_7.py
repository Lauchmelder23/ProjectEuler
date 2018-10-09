######################################################################
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
######################################################################

primeIndex = 0
prime = 0
iterator = 2

while primeIndex <= 10001:
    isPrime = True
    for i in range(2, int(iterator / 2)):
        if iterator % i is 0:
            isPrime = False
            break

    if isPrime is True:
        prime = iterator
        primeIndex += 1

    iterator += 1

print(prime)
# Solution: 104743
