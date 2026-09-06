def g(x):
    return x - 2

summ = 0

# range(2, 33, 3) gir x-verdiene 2, 5, 8, ..., 32
for i in range(2, 33, 3):
    summ += g(i) * 3

print(summ)
