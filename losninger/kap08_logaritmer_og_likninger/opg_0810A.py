def f(x):  # Ordinær konto
    return 5000*1.01**x

def g(x):  # Høyrentekonto
    return 2500*1.02**x

aar = 5

# Vi øker antall år så lenge det er mest penger på den ordinære kontoen
while f(aar) > g(aar):
    aar += 1

print(f"Etter {aar} år er det mest penger på høyrentekontoen.")
print(f"Ordinær konto:  {f(aar):.2f} kr")
print(f"Høyrentekonto: {g(aar):.2f} kr")
