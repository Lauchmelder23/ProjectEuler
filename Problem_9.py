######################################################################
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
######################################################################

for a in range(1, 1000):
    for b in range(1, 1000 - a):
        c = 1000 - a - b

        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print(a*b*c)
            exit()


# Solution: 31875000
