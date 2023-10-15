import math

vinkler = [0, 30, 45, 60, 90]
for vinkel in vinkler:
    vinkel_radianer = vinkel * 2 * math.pi / 360
    sin_verdi = math.sin(vinkel_radianer)
    print(f"Vinkel: {vinkel} grader, Sinus: {sin_verdi}")