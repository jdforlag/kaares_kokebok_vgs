def h(x):
    return x**2 / (x - 2)

x1 = 3
x2 = 6
n = 15
dx = (x2 - x1) / n
summ = 0

for i in range(n):
    x = x1 + i*dx   # x = 3, 3+dx, 3+2dx, ..., 6-dx
    summ += h(x) * dx

print(f"Rektangelsummen er {summ:.4f}")
