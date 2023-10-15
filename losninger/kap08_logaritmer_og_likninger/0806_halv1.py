# Endrer startverdien for 'b' og gjentar algoritmen 10 ganger.
a = -3
b = 4  

for _ in range(25):  # 25 iterasjoner er nok
    m = (a + b) / 2
    print(f"{m:.6f}")
    if a * m < 0:
        b = m
    elif b * m < 0:
        a = m

