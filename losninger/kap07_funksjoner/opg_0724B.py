# Marius stabler boksene i en flat pyramide:
# øverste etasje har 1 boks, neste 2 bokser, så 3, og så videre.
# Etasje nr. n (talt ovenfra) har altså n bokser.

def bokser(n):
    """Antall bokser i etasje nr. n, talt ovenfra."""
    return n

# Kontroll mot figuren, som viser et tårn med 4 etasjer
print(f"Tårnet på figuren har {bokser(1) + bokser(2) + bokser(3) + bokser(4)} bokser.")

# Hvor mange bokser trenger Marius til et tårn med 20 etasjer?
totalt = 0
for etasje in range(1, 21):
    totalt += bokser(etasje)

print(f"Et tårn med 20 etasjer krever {totalt} bokser.")

# Hvor høyt tårn klarer han med 400 bokser?
brukte_bokser = 0
etasjer = 0

# Legger på en ny etasje så lenge vi har nok bokser igjen til hele etasjen
while brukte_bokser + bokser(etasjer + 1) <= 400:
    etasjer += 1
    brukte_bokser += bokser(etasjer)

print(f"Med 400 bokser blir det største tårnet {etasjer} etasjer høyt.")
print(f"Da bruker Marius {brukte_bokser} bokser, og har {400 - brukte_bokser} til overs.")
