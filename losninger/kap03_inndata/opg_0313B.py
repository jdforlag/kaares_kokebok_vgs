tall = int(input("Oppgi et tresifret tall: "))
siffer1 = tall // 100
siffer2 = (tall % 100) // 10
siffer3 = tall % 10
tverrsum = siffer1 + siffer2 + siffer3
print(f"Tverrsummen er {tverrsum}.")
