def f(x):
    return x**2 + 1

dx = 2   # Avstanden mellom x-verdiene
summ = 0

# x-verdiene er 1, 3, 5, ..., 15
for x in range(1, 16, 2):
    summ += f(x) * dx

print(f"Summen er {summ}")
