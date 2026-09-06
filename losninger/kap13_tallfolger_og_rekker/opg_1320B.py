a = 100  # Tilbud A, uke 1
b = 100  # Tilbud B, uke 1

print("Uke   Tilbud A   Tilbud B")
for uke in range(1, 5):
    print(f"{uke:3}   {a:8.2f}   {b:8.2f}")
    a = a + 10      # Rekursiv formel for tilbud A
    b = b * 1.05    # Rekursiv formel for tilbud B

# Vi starter på nytt, og teller opp til tilbud B gir mest
a = 100
b = 100
uke = 1

while b <= a:
    a = a + 10
    b = b * 1.05
    uke += 1

print(f"Fra uke {uke} gir tilbud B mer ukelønn enn tilbud A.")
print(f"Uke {uke}: tilbud A gir {a:.2f} kr og tilbud B gir {b:.2f} kr.")
