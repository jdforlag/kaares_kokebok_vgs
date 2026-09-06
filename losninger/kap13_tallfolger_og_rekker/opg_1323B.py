a1 = float(input("Oppgi a1: "))
d = float(input("Oppgi d: "))

S = 0
for n in range(1, 11):
    a = a1 + d*(n-1)   # Det generelle uttrykket for ledd nr. n
    print(f"a{n} = {a}")
    S = S + a

print(f"Summen av de 10 første leddene er {S}")
