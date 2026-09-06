leddnr = int(input("Oppgi leddnr: "))
S = 0
for i in range(1, leddnr+1):
    a = 4*i - 3   # Det i-te leddet
    S = S + a     # Legger leddet til summen

print(f"S_{leddnr} = {S}")
