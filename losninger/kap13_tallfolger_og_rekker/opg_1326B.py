fib = [0, 1]
n = 2

# Lager nye Fibonacci-tall så lenge summen er 250 000 eller mindre
while sum(fib) <= 250_000:
    fib.append(fib[n-1] + fib[n-2])
    n += 1

print(fib)
print(f"Summen av tallene er {sum(fib)}")
print(f"Det var nødvendig med {len(fib)} ledd.")
