antall_skruer = [60, 120, 250, 500, 960]
priser = [329.4, 658.8, 1098.0, 1647.0, 2470.5]
forhold = [priser[i] / antall_skruer[i] for i in range(len(antall_skruer))]
print("Forholdet mellom priser og antall skruer:", forhold)
