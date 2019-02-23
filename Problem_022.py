#######################################################################
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
# five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
######################################################################


with open("data/p022_names.txt", "r") as f:
    names = f.readline().replace('"', '').split(',')

names.sort()

total_name_scores = 0
for pos in range(0, len(names)):
    name_score = 0
    for letter in names[pos]:
        name_score += ord(letter) - 64

    name_score *= (pos + 1)
    total_name_scores += name_score

print(total_name_scores)