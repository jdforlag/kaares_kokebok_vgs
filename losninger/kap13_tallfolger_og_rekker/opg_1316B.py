def a(n):
    return 8*n - 1

summ = 0
leddnr = 1

# Det siste leddet i rekka er 399
while a(leddnr) <= 399:
    summ += a(leddnr)
    leddnr += 1

print(f"Summen er {summ}")
print(f"Rekka har {leddnr - 1} ledd.")
