######################################################################
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
######################################################################

maxProduct = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        product = str(i*j)

        if product == product[::-1]:
            if int(product) > maxProduct:
                maxProduct = int(product)

print(maxProduct)
# Solution: 906609
