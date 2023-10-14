billettype = input("Du kan velge mellom dagskort(d) eller 3-timers kort(k). Oppgi ønsket billettype (d/k): ")
alder = int(input("Oppgi alder: "))

if billettype == "d":
    if alder >= 16:
        pris = 420
    else:
        pris = 200
elif billettype == "k":
    if alder >= 16:
        pris = 250
    else:
        pris = 120

print(f"Din billettpris er {pris} kr.")