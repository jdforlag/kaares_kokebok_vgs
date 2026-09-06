def f(x):
    return -0.1*x**2 + 100*x - 3000

# Finner den minste produksjonen som gir mer enn 15 000 kr i overskudd
x = 0
while f(x) <= 15_000:
    x += 1

nedre = x
print(f"Overskuddet passerer 15 000 kr ved {nedre} enheter.")
print(f"Overskudd ved {nedre} enheter: {f(nedre):.2f} kr")

# f er en andregradsfunksjon med toppunkt, så overskuddet synker igjen.
# Vi finner derfor også den øvre grensa.
while f(x) > 15_000:
    x += 1

ovre = x - 1  # Siste antall enheter som fortsatt gir over 15 000 kr
print(f"Overskuddet er over 15 000 kr for {nedre}-{ovre} enheter.")
