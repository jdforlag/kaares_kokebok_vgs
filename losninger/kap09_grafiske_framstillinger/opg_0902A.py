import matplotlib.pyplot as plt

dager = ["Mandag", "Tirsdag", "Onsdag"]
kebaber = [41, 93, 29]

plt.bar(dager, kebaber)
plt.ylabel("Antall solgte kebab")
plt.title("Kebabsalg hos Sultan Snackbar")
plt.show()
