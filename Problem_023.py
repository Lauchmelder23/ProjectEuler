import math

abundant = []

for i in range(1, 28124):
    divisors = []
    for j in range(1, math.ceil(i / 3) + 1):
        if i % j == 0:
            divisors.append(j)
            if j != 1:
                divisors.append(i / j)

    divisors = list(set(divisors)) # Remove duplicates
    if sum(divisors) > i:
        abundant.append(i)

sums = []
for i in range(0, len(abundant)):
    for j in range(i, len(abundant)):
        sums.append(abundant[i] + abundant[j])

sums = list(set(sums)) # Remove dupliactes

final_sum = 0
for i in range(1, 28124):
    if i not in sums:
        final_sum += i

print(final_sum)