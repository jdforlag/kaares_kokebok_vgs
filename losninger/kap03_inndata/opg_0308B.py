pris = float(input("Oppgi pris: "))
rabatt_prosent = float(input("Oppgi prosent rabatt: "))
rabatt_kr = pris * (rabatt_prosent / 100)
ny_pris = pris - rabatt_kr
print(f"Du får {rabatt_kr:.2f} kr i rabatt")
print(f"Den nye prisen er {ny_pris:.2f} kr")
