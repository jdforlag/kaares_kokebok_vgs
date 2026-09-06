valg = ["stein", "saks", "papir"]
mulige = 0

for spiller in valg:
    for cpu in valg:
        # Viser kombinasjonen
        print(f"Spiller valgte: {spiller}, CPU valgte: {cpu}")
        mulige += 1

print(f"{mulige = }")
