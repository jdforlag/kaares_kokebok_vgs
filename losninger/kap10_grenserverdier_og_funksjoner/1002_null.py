def f(x):
    return 1/x

print(f(0.1))
print(f(-0.1))

a = 4.0
for _ in range(344):
    print(f(a))
    a = a / 8
