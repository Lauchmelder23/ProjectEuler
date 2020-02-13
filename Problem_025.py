a = 1
b = 1
c = 2

index = 3
while True:
    a = b
    b = c
    c = a + b
    index += 1
    if len(str(c)) >= 1000:
        break

print(index)
# Solution: 4782