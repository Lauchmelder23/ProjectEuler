######################################################################
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
# letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out
# numbers is in compliance with British usage.
######################################################################

ones = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
special_tens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN",
                "NINETEEN"]
tens = ["TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
hundreds = ["ONEHUNDREDAND", "TWOHUNDREDAND", "THREEHUNDREDAND", "FOURHUNDREDAND", "FIVEHUNDREDAND", "SIXHUNDREDAND",
            "SEVENHUNDREDAND", "EIGHTHUNDREDAND", "NINEHUNDREDAND"]



letter_count = 0
for one in ones:
    letter_count += len(one)

for ten in special_tens:
    letter_count += len(ten)

for ten in tens:
    letter_count += len(ten)
    for one in ones:
        letter_count += len(one) + len(ten)

for hundred in hundreds:
    letter_count += len(hundred) - 3

    for one in ones:
        letter_count += len(hundred) + len(one)

    for ten in special_tens:
        letter_count += len(hundred) + len(ten)

    for ten in tens:
        letter_count += len(hundred) + len(ten)
        for one in ones:
            letter_count += len(hundred) + len(ten) + len(one)

letter_count += len("ONETHOUSAND")


print(letter_count)
# Solution: 21124
