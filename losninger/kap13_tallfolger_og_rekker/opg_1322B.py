def a(n):
    return 6*n / (-2)**n

S = 0
for n in range(1, 21):
    ledd = a(n)
    S = S + ledd
    print(f"a{n} = {ledd}, S{n} = {S}")

# Av utskriften ser vi at
#     lim (n -> uendelig) a_n = 0
#     lim (n -> uendelig) S_n = -4/3 = -1,3333...
print(f"Til sammenligning er -4/3 = {-4/3}")
