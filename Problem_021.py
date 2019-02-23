##########################################################################
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
##########################################################################


def sumDivisors(x):
    divisor_sum = 0
    for j in range(1, int(x / 2) + 2):
        if (x % j) is 0:
            divisor_sum += j

    return divisor_sum


amicable_number = []
for i in range(1, 10000):
    if i in amicable_number:
        continue

    testing_number = sumDivisors(i)
    if (i == sumDivisors(testing_number)) and (testing_number != i):
        amicable_number.append(i)

        if testing_number not in amicable_number:
            amicable_number.append(testing_number)

sum_of_numbers = sum(amicable_number)
print(sum_of_numbers)

# Solution: 31626
