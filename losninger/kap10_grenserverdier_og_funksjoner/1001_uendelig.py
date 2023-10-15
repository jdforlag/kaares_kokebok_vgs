def h(x):
    return (3*x**2-2) / (x**2-5*x)

a = 2.0

for i in range(20):
    a = a * 10
    print(h(a))

print("\nUtforsker grenseverdien for negative verdier av x:")
a = -2.0
for i in range(17):
    a = a * 10
    print(h(a))
