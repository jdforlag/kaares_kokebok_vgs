timer, minutter = input("Oppgi klokkeslett: ").split(":")
timer = int(timer)
minutter = int(minutter)
timer_til_midnatt = 23 - timer + (60 - minutter) / 60
print(f"Det er {timer_til_midnatt:.1f} timer igjen til midnatt.")
