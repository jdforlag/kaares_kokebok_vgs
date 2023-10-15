saldo = 0
for maaned in range(1, 21):
    saldo += 300
    saldo *= 1.005
    print(f"Måned {maaned}: {saldo:.2f} kr")