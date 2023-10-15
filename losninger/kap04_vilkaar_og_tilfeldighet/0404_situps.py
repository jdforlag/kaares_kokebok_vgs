situps = int(input("Hvor mange sit-ups klarte du på 1 minutt? "))

if situps > 49:
    print("Utmerket")
elif situps >= 44:
    print("Bra")
elif situps >= 39:
    print("Over gjennomsnittet")
elif situps >= 31:
    print("Gjennomsnittlig")
elif situps >= 25:
    print("Under gjennomsnittet")
else:
    print("Veldig svakt")
