sum = 0
n = 1
while sum <= 10000000:
    an = n ** 2 - 3 * n + 2
    sum += an
    n += 1
print(n)