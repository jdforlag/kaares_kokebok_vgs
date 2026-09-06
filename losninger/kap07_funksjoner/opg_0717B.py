def f(x):
    return x**0.5

# Gjennomsnittlig vekstfart til f i [x1, x2]
def gvf(x1, x2):
    endring_x = x2 - x1
    endring_y = f(x2) - f(x1)
    return endring_y / endring_x

for i in range(10):
    gjsnittvf = gvf(i, i+1)
    print(f"Intervall: [{i}, {i+1}], GVF: {gjsnittvf:.2f}")
