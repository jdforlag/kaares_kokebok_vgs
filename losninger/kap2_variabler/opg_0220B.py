mel = 750
egg = 12
melk = 15
porsjoner_mel = mel // 100
porsjoner_egg = egg // 2
porsjoner_melk = melk // 3
totalt_porsjoner = min(porsjoner_mel, porsjoner_egg, porsjoner_melk)
print(f"Vigdis kan lage {totalt_porsjoner} hele porsjoner vafler.")