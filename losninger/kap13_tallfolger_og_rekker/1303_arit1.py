a = 2
summ = 0

# Prøv deg fram med antall iterasjoner til
# det siste tallet er 186
for i in range(24):
    print(a, end=" ")
    summ += a
    a += 8  # Beregner det neste tallet i rekka

print()  # Skriver ut en ny linje for lesbarhet
print(f"Summen er {summ}")

