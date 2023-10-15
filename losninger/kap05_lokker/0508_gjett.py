import random

tall = random.randint(0, 100)
forsok = 1
gjett = int(input("Gjett på tallet (0-100):"))

while gjett != tall:  # Så lenge brukeren gjetter feil ...
    if gjett < tall:
        print("For lavt!")
    elif gjett > tall:
        print("For høyt!")
    print("Feil tall, prøv igjen")
    gjett = int(input("Gjett på tallet (0-100):"))
    forsok += 1
    
print("Du gjettet riktig!")
print(f"Det tok deg {forsok} forsøk.")
