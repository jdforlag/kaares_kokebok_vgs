a = 100
k = 0.9
S = 0
for n in range(20):
    S = S + a
    a = a * k
print(f"S_20 = {S}")
