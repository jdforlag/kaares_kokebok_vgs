tall = input("Oppgi et tresifret tall: ")
tall2 = int(tall + tall)

if tall2 % 7 == 0 and tall2 % 11 == 0 and tall2 % 13 == 0:
    tall2 //= (7 * 11 * 13)
    print(f"Tallet {tall2} er delelig med 7, 11 og 13")
else:
    print("Tallet er ikke delelig med 7, 11 og 13")