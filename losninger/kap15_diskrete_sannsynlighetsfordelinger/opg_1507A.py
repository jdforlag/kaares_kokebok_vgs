k = 0
while True:
    sanns = [k, 0.3, k-0.2, 0.1]
    sum_sanns = sum(sanns)

    # Summen av alle sannsynlighetene i en fordeling skal være 1
    if abs(sum_sanns - 1) < 0.01:
        print(f"k = {k:.2f}")
        break

    k += 0.01
