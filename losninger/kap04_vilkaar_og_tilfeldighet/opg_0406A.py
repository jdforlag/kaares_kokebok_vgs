import random

tall1 = random.randint(1, 10)
tall2 = random.randint(1, 10)
fasit = tall1 * tall2

print(f"{tall1}*{tall2} =")
svar = int(input())

if svar == fasit:
    print("Riktig")
else:
    print("Feil")