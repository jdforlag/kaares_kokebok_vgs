tallene = [2, 6, 1, -5, 3, 10, 2, 9, -11]
tallene.sort()  # Sorterer tallene i stigende rekkefølge

while len(tallene) >= 3:
    print(*tallene)
    tallene.pop(0)  # Fjerner det minste tallet
    tallene.pop()
    
median = tallene[0]  # Henter medianen
print("Medianen er:", median)

