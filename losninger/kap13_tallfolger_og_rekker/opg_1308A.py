k = float(input("Oppgi k: "))

# En uendelig geometrisk rekke konvergerer bare når kvotienten
# ligger mellom -1 og 1
if -1 < k < 1:
    print("Rekka er konvergent")
else:
    print("Rekka er ikke konvergent")
