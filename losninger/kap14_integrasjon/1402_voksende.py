trapes_bredde = 5  # Total bredde av trapeset
hoyde_diff = 1 # Høydeforskjell fra det laveste til det høyeste rektanglet
antall_rekt = 13  # 13 rektangler gir differansen mindre enn 0,2

bredde = trapes_bredde / antall_rekt
hoydeokning = hoyde_diff / antall_rekt  # Dette antar en jevn fordeling av total høyde

hoyde = 1  # Høyden til det første rektanglet
areal_sum = 0

for _ in range(antall_rekt):
    areal_sum += hoyde * bredde
    hoyde += hoydeokning

# Skriver ut summen av rektanglene
print("Rektangelsum:", areal_sum)
trapes = 7.5  # Dette er basert på trapesformelen gitt i oppgaven
diff = trapes - areal_sum
# Skriver ut relevant informasjon
print("Trapes:", trapes)
print("Differanse:", diff)
