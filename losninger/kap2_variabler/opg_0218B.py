migranter = 137
rom_storrelse = 6
fulle_rom = migranter // rom_storrelse
siste_rom = migranter % rom_storrelse
print(f"Antall fulle rom: {fulle_rom}, antall migranter i siste rom: {siste_rom}")