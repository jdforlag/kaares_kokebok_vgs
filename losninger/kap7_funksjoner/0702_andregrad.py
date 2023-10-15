def h(x):
    return x**2 - 4*x

print("h(x) = x**2 - 4*x")
print(f"{h(3) = }")
print(f"{h(0) = }")

print("x, h(x)")
print("-------")

summ = 0

for i in range(-2, 6):
    print(f"{i}, {h(i)}")
    summ += h(i)

print(f"{summ = }")
