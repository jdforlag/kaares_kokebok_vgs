kar = [2, 5, 4, 6, 5, 4, 4, 2, 3]
# Legger til eksamenskarakterer
for i in range(8):
    kar.append(4)
    
antall_kar = len(kar)
print(f"Antall karakterer: {antall_kar}")
sum_kar = sum(kar)
print(f"Karaktersum: {sum_kar}")
gjennomsnitt = sum_kar / antall_kar
print(f"Snittet: {gjennomsnitt:.2f}")


