def a(n):
    return 6 * n - 4

# Beregner summen for hvert tredje ledd fra a_5 til 656
summ = 0
i = 5  # Starter med a_5
while a(i) <= 656:
    summ += a(i)
    i += 3  # Hopper over to ledd hver gang (får hvert tredje ledd)

print(f"Summen er {summ}")
