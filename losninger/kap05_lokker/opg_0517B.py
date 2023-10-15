import random
import math

tall = random.randint(0, 121)
fasit = round(math.sqrt(tall), 1)

while True:
    gjett = float(input(f"Gjett kvadratroten av {tall}, avrundet til 1 desimal: "))
    if gjett < fasit:
        print("For lavt! Prøv igjen.")
    elif gjett > fasit:
        print("For høyt! Prøv igjen.")
    else:
        print("Korrekt!")
        break