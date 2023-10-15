sekunder_total = 15333
timer = sekunder_total // 3600
minutter = (sekunder_total % 3600) // 60
sekunder = sekunder_total % 60
print(f"{sekunder_total} sekunder er {timer} timer, {minutter} minutter, og {sekunder} sekunder.")