a1 = float(input("Oppgi a1: "))
k = float(input("Oppgi k: "))

for n in range(1, 9):
    a = a1 * k**(n-1)   # Det generelle uttrykket for ledd nr. n
    print(f"a{n} = {a}")

if -1 < k < 1:
    print("Rekka er konvergent")
else:
    print("Rekka er ikke konvergent")
