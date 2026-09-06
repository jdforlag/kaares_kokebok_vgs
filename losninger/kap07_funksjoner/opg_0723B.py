def f(x):
    return (2*x - 3) / (4 - x)

x = 5

# Vi dobler x for hver iterasjon: 5, 10, 20, 40, ...
for i in range(60):
    print(f(x))
    x = x * 2

# Med 10 iterasjoner ser vi at verdiene nærmer seg -2.
# Med 60 iterasjoner ser vi tydelig at f(x) går mot -2 når x går mot uendelig.
