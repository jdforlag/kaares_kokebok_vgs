fart = float(input("Oppgi fart: "))
fartsgrense = 80
print(f"Din fart er {fart} km/t")

if fart > fartsgrense:
    overskridelse = fart - fartsgrense
    print(f"Senk farten! Du kjører {overskridelse:.1f} km/t over fartsgrensen.")
