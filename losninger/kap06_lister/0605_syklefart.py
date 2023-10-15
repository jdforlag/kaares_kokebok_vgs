distanser = [20, 18, 34, 10, 42, 13, 9]  # I kilometer
tider = [41, 66, 61, 19, 82, 25, 23]  # I minutter
antall_turer = len(distanser)

fart_liste = []

for i in range(antall_turer):
    fart_kmpermin = distanser[i] / tider[i]
    fart_kmpertime = fart_kmpermin * 60
    fart_liste.append(fart_kmpertime)

print("Fartslista:", *fart_liste)
