
karakterer = input("Oppgi dine karakterer: ").split()
karakterer = [int(karakter) for karakter in karakterer]
gjennomsnitt = sum(karakterer) / len(karakterer)
print(f"Du skrev inn {len(karakterer)} karakterer")
print(f"Gjennomsnittskarakteren din er {gjennomsnitt:.1f}")
