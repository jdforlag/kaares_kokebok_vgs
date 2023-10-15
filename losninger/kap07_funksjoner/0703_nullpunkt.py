def g(x):
    return -23.4 + (7/3)*x

# Test funksjonen for ulike verdier av x
print(f"{g(0) = }")

a = 0  # Starter med en initiell verdi for a

# Øker verdien av 'a' til vi finner et nullpunkt
while g(a) < 0:
    a += 0.001  # Dette trinnet kan justeres for mer nøyaktige resultater

print(round(g(a), 3))
# Skriver ut verdien av 'a' som er vår tilnærmede løsning på nullpunktet
print(f"Nullpunktet er x = {a:.3f}")
