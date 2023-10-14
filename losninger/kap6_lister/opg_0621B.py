figurer = []
sum_k = 0  # Summen av kvadrattallene

# Regner ut antall blokker for de 10 første figurene
for i in range(1, 11):
    sum_k += i**2
    figurer.append(sum_k)

# a) Blokker i figur 5
print(f"Det er {figurer[4]} klosser i figur nr 5.")

# b) Totalt antall blokker i de første 10 figurene
sum10 = sum(figurer)
print(f"Det er {sum10} klosser i de 10 første figurene til sammen.")

# c) Antall figurer 10 000 blokker gir
total_blocks = 10000
num_figures = 0
remaining_blocks = total_blocks

for blocks in figurer:
    if remaining_blocks >= blocks:
        num_figures += 1
        remaining_blocks -= blocks
    else:
        break

print(f"Roar kan lage {num_figures} figurer.")
print(f"Han vil ha {remaining_blocks} klosser igjen når han har laget figurene.")
