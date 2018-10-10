######################################################################
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
#
######################################################################

divideBy = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
maxNumber = 20

while True:
    divisible = True
    for divisor in divideBy:
        if maxNumber % divisor is not 0:
            divisible = False
            break

    if divisible is True:
        break

    maxNumber += 20

print(maxNumber)
# Solution: 232792560
