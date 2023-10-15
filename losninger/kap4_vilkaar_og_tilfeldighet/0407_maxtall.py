import random

a = random.randint(1, 50)
b = random.randint(1, 50)
c = random.randint(1, 50)

print(f"a = {a}, b = {b}, c = {c}")

if a > b and a > c:
    print("a er størst")
elif b > a and b > c:
    print("b er størst")
else:
    print("c er størst")
