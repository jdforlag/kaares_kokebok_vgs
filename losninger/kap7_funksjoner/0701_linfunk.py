def g(x):
    return 5 - 2*x

gjett = int(input("Hva er konstantleddet? "))
konst = g(0)

if gjett == konst:
    print("Det er riktig!")
else:
    print(f"Det er feil. Konstantleddet er {konst}.")
