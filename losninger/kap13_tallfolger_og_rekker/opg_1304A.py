# range(start, stopp, steg) gir tallene fra start, i steg, opp til (men ikke
# med) stopp. Vi må derfor sette stoppverdien til 62 for å få med 61.
for tall in range(6, 62, 5):
    print(tall, end=" ")
