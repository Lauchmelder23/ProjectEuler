######################################################################
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
######################################################################

primes = [1]
original = 600851475143

for x in range(1, int(original / 2)):
    print(x)
    tester = 600851475143
    for prime in primes:
        tester /= prime

    if x > tester:
        break

    if int(original) % x is 0:
        primes.append(x)
        original /= x

print("{}".format(primes))
# Solution: 6857
