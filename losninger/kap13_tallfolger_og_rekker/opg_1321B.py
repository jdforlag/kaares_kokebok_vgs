def S(n):
    """Mengden virkestoff i kroppen rett etter tablett nummer n."""
    a1 = 7      # Første tablett gir 7 mg
    k = 0.9     # 10 % brytes ned hvert døgn, så 90 % er igjen
    return a1 * (k**n - 1) / (k - 1)

# Kontroll mot tabellen i oppgaven
print(f"Tablett 1: {S(1):.2f} mg")
print(f"Tablett 2: {S(2):.2f} mg")
print(f"Tablett 3: {S(3):.2f} mg")

# Hvordan utvikler mengden seg videre?
for n in [10, 25, 50, 100, 500]:
    print(f"Tablett {n}: {S(n):.2f} mg")

# Mengden nærmer seg summen av den uendelige geometriske rekka:
#     a1 / (1 - k) = 7 / 0,1 = 70 mg
# Mengden kommer altså aldri over 100 mg. Legen har rett.
print(f"Den uendelige summen er {7 / (1 - 0.9):.0f} mg.")
