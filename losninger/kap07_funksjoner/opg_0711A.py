# Forklaring:
# Programmet definerer funksjonen f(x) = x**2 og starter med x = 1.
# Så lenge f(x) er mindre enn eller lik 400, skriver programmet ut f(x)
# og øker deretter x med 1.
# Resultatet blir kvadrattallene 1, 4, 9, 16, ..., 400.
# Løkka stopper når x = 21, fordi f(21) = 441, og 441 > 400.

def f(x):
    return x ** 2

x = 1
while f(x) <= 400:
    print(f(x))
    x = x + 1
