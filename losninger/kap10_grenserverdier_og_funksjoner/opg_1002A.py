k = 1.0
a = 3.0 + k

# a nærmer seg 3 ovenfra, altså x -> 3+
while a > 3.01:
    print(a)
    k = k / 4
    a = 3.0 + k

print(a)  # Den siste verdien, som er nærmest 3
