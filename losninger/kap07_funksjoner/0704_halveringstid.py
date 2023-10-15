def c(t):
    """Beregner konsentrasjonen av medisin i mg etter t timer."""
    return 100 * (1/2)**(t/4)

print(f"{c(0) = }")
print(f"{c(4) = }")

kons16 = c(16)
print(f"Konsentrasjonen av medisin etter 16 timer er {kons16} mg.")

timer = 0
while c(timer) >= 1:
    timer += 1

print(f"Det tar {timer} timer før konsentrasjonen av medisinen går under 1 mg, og David må ta en ny dose.")
