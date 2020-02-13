digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def permutate(symbols, prev=""):
    if len(symbols) == 1:
        return [int(prev + str(symbols[0]))]

    perms = []
    for symbol in symbols:
        orig = symbols.copy()
        orig.remove(symbol)
        perms += permutate(orig, prev=prev+str(symbol))

    return perms

permutations = sorted(permutate(digits))
print(permutations[999999])
# Solution: 2783915460