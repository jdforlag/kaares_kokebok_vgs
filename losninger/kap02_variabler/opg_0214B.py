gallon_per_fat = 42
liter_per_gallon = 3.785
fat = 100 * 10**6
gallon = fat * gallon_per_fat
liter = gallon * liter_per_gallon
print(f"Antall liter: {liter:.2e}")