# Leser inn tall fra brukeren og konverterer til heltall
tallA = int(input("Oppgi et tall: "))
tallB = int(input("Oppgi et tall til: "))
tallC = int(input("Oppgi enda et tall: "))

# Beregner summen av de tre tallene
summen = tallA + tallB + tallC

# Skriver ut summen på en formatert måte
print(f"{tallA} + {tallB} + {tallC} = {summen}")