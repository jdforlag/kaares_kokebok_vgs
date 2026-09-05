def i(x):
    return 200*x

def k(x):
    return 0.3*x**2 + 20*x + 10_000

# Finner den første produksjonsmengden der inntektene er større enn kostnadene
x1 = 0
while i(x1) < k(x1):
    x1 += 1

# Fortsetter så lenge vi har overskudd, og går deretter ett steg tilbake
x2 = x1
while i(x2) > k(x2):
    x2 += 1
x2 -= 1  # Siste produksjonsmengde som fortsatt gir overskudd

print(f"Bedriften har overskudd når x er mellom {x1} og {x2}.")
print(f"Overskudd ved x = {x1}: {i(x1) - k(x1):.2f} kr")
print(f"Overskudd ved x = {x2}: {i(x2) - k(x2):.2f} kr")
