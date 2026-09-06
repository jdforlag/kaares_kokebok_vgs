def f(x):
    return (5 - 3*x) / (6*x + 1)

x = 1
for i in range(15):
    print(f"x = {x}, f(x) = {f(x)}")
    x = x * 10  # x vokser med en faktor 10

# Verdiene nærmer seg -0,5. Grenseverdien er altså
#     lim (x -> uendelig) (5-3x)/(6x+1) = -3/6 = -0,5
