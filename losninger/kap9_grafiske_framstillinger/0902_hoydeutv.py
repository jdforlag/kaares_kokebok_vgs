import matplotlib.pyplot as plt

# Definerer alder da høyden ble målt
alder = [4, 6, 7, 10, 15]

# Definerer de tilsvarende høydene
hoyder = [101, 122, 128, 140, 154]

# Tegner linjediagrammet basert på de definerte verdiene
plt.plot(alder, hoyder)
plt.grid()
plt.xlabel("Alder (år)")
plt.ylabel("Høyde (cm)")
plt.title("Vivians høydeutvikling")
# Viser linjediagrammet
plt.show()
