# Vi deler hver figur i tre deler, og finner et mønster for hver del:
#   hodet er et kvadrat:      1x1,  2x2,  3x3   ->  n*n
#   halen er en diagonal:     1,    2,    3     ->  n
#   kroppen er et rektangel:  3x2,  5x3,  7x4   ->  (2n+1) rader ganger (n+1)
#                             ...der ett kvadrat mangler nederst i midten
#
# Figur 1 får da 1 + 1 + (3*2 - 1) = 7 små kvadrater,
# figur 2 får 4 + 2 + (5*3 - 1) = 20, og figur 3 får 9 + 3 + (7*4 - 1) = 39.

def f(n):  # Antall små kvadrater i figur nr n
    hode = n**2
    hale = n
    kropp = (2*n+1) * (n+1) - 1
    return hode + hale + kropp

# Kontroll mot figurene i oppgaven
print(f"{f(1) = }")
print(f"{f(2) = }")
print(f"{f(3) = }")

sum_kvadrater = 0
for fignr in range(1, 101):
    sum_kvadrater = sum_kvadrater + f(fignr)

print(f"De 100 første figurene krever {sum_kvadrater} små kvadrater.")
