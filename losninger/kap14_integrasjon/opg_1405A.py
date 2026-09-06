def g(x):
    return x**2 - 4*x

a = 0
b = 4
n = 10
delta_x = (b - a) / n
areal_sum = 0

for i in range(n):
    x = a + i * delta_x
    areal_sum += g(x) * delta_x

print(areal_sum)
