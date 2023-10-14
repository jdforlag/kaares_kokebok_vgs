leil_totalt = 40
leil_2rom = int(input("Antall 2-roms: "))
leil_3rom = leil_totalt - leil_2rom
rom = 2 * leil_2rom + 3 * leil_3rom
print("Antall 3-roms:", leil_3rom)
print("Antall rom:", rom)
