print("Oppgi et heltall a > 2.")
original_a = int(input("a = "))
a = original_a
faktorer = []

# Prime factorization
for divisor in range(2, a+1):
    while a % divisor == 0:
        faktorer.append(divisor)
        a = a // divisor
    if a == 1:  # Done factorizing
        break

# Python trick to join the factors with '*'
txt = " * ".join(map(str, faktorer))
print(f"{original_a} = {txt}")
