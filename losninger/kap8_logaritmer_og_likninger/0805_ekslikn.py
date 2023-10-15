def vs(x):
    return 5000 * 1.03 ** x

def hs(x):
    return 2500 * 1.06 ** x

# Skriver ut verdien av høyresiden når x = 0
print(hs(0))

# Beregner og skriver ut forskjellene for x i {0, 5, ..., 50}
for i in range(0, 51, 5):
    diff = vs(i) - hs(i)
    print(f"x={i}, diff={diff:.2f}")

i = 0
while vs(i) - hs(i) > 0:
    i += 0.001  # Økning på 0,001

print(i)  # 24.14...




