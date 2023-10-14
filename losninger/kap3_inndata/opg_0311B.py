import math

a = float(input("Oppgi lengden av den første korte siden: "))
b = float(input("Oppgi lengden av den andre korte siden: "))
c = math.sqrt(a ** 2 + b ** 2)
print(f"Den lengste siden er {c:.1f}.")
