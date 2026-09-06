# a) Mona går gjennom alle de 6*6 = 36 mulige utfallene når to terninger
#    kastes, og øker telleren g hver gang summen av øynene er 8 eller mer.
#    Til slutt deler hun antall gunstige på antall mulige. Hun regner altså ut
#        P(sum av øyne >= 8) = 15/36 = 0,4167

g = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i+j >= 8:
            g = g + 1

print(g/36)

# b) Med tre terninger er det 6*6*6 = 216 mulige utfall. Vi bruker tre
#    løkker inni hverandre og teller opp utfallene som gir summen 7 eller 11.
gunstige = 0
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i+j+k == 7 or i+j+k == 11:
                gunstige += 1

print(f"Antall gunstige utfall: {gunstige}")
print(f"Sannsynligheten for å vinne er {gunstige}/216 = {gunstige/216:.4f}")
