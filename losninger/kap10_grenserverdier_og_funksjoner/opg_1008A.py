# Svar:
# Uttrykket (K(x+h) - K(x)) / h er den numeriske deriverte til K, altså
# grensekostnaden: hvor mye det koster å produsere én enhet til.
# Løkka øker x så lenge grensekostnaden er mindre enn 260 kroner.
#
# Resultatet blir 300.
#
# Det forteller bedriften at grensekostnaden er under 260 kroner så lenge
# de produserer færre enn 300 enheter per uke. Ved 300 enheter koster det
# 260 kroner å produsere den neste enheten.

def K(x):
    return 0.2*x**2 + 140*x + 7000

v = 260
h = 0.0001
x = 0

while (K(x+h) - K(x)) / h < v:
    x = x + 1

print(x)
