# Likningen 4**(t**2) = 4**(6-t) er oppfylt når eksponentene er like,
# altså når t**2 = 6 - t. Programmet prøver alle heltallene fra -10 til 10.

for t in range(-10, 11):
    vs = 4**(t**2)
    hs = 4**(6-t)
    if hs == vs:
        print(t)
