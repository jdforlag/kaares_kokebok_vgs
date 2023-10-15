alder = int(input("Hvor gammel er du? "))
hoyde = int(input("Hvor høy er du (i cm)? "))

if alder >= 12 or hoyde > 140:
    print("Du kan kjøre karusellen")
else:
    print("Beklager, du kan ikke kjøre karusellen.")
