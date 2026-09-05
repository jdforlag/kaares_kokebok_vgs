def h(x):
    return x**2 - 2

# Vi gjør dx mindre for å få flere riktige desimaler i svaret.
# Med dx = 0,0001 finner vi nullpunktet med 4 riktige desimaler.
dx = 0.0001  # Endring i x for hver iterasjon av løkka
a = 0
x_slutt = 4

while a < x_slutt:
    # Har h(a) og h(a+dx) ulike fortegn, blir produktet negativt.
    # Da må grafen ha krysset x-aksen mellom a og a+dx.
    if h(a) * h(a+dx) <= 0:
        print(f"Nullpunktet er x = {a:.4f}")
    a += dx
