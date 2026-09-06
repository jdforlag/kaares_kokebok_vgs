a = 3    # Det første leddet
k = -2   # Kvotienten
S = 0

for n in range(8):
    S = S + a
    a = a * k

print(f"S_8 = {S}")
