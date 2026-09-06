def g(x):
    return 4-x

def rekt_sum(x_min, x_maks, antall_rekts):
    bredde = (x_maks - x_min) / antall_rekts
    sum_areal = 0
    xn = x_min
    for i in range(antall_rekts):
        hoyde = g(xn)
        sum_areal += hoyde * bredde
        xn += bredde
    return sum_areal

# Test av funksjonen
print(rekt_sum(0, 4, 2))
print(rekt_sum(0, 4, 8))
