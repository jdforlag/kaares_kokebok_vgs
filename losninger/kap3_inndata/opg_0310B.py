import math

L = float(input("Oppgi snorlengden i meter: "))
g = 9.81
T = 2 * math.pi * math.sqrt(L / g)
print(f"Svingetiden er {T:.2f} sekunder.")
