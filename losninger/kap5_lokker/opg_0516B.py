tall = int(input("Skriv inn et heltall større enn 2: "))
primtall = True
for deletall in range(2, tall):
    if tall % deletall == 0:
        primtall = False
        break
if primtall:
    print(f"{tall} er et primtall.")
else:
    print(f"{tall} er ikke et primtall.")