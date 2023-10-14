fotlengde = float(input("Oppgi fotlengde i cm: "))
skrittlengde = float(input("Oppgi skrittlengde i cm: "))

hoyde = 7 * fotlengde
hoftehoyde = 4 * fotlengde
relativ_skrittlengde = skrittlengde / hoftehoyde

print(f"Estimert høyde: {hoyde} cm")

if relativ_skrittlengde < 2:
    print("Sannsynligvis gikk personen")
elif relativ_skrittlengde > 2.9:
    print("Sannsynligvis løp personen")
else:
    print("Bevegelsestypen er uavklart")