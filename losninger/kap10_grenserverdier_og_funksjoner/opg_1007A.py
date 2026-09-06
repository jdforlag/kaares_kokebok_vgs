def B(x):
    return 70000*1.003**x

mnd = 0

# Teller opp én måned av gangen til beløpet har passert 80 000 kr
while B(mnd) < 80_000:
    mnd = mnd + 1

print(f"Det tar {mnd} måneder før Knut har 80 000 kroner.")
print(f"Da har han {B(mnd):.2f} kr.")
