# a) Lars vil finne nullpunktene til f, altså de x-verdiene der f(x) = 0.
#    Programmet går gjennom heltallene x = 0, 1, 2, ..., 10, og skriver ut
#    x-verdien dersom f(x) = 0.
#    For f(x) = 3x - 15 skriver programmet ut 5, siden f(5) = 3*5 - 15 = 0.
#
# b) Med f(x) = x**2 - 6x + 8 skriver programmet ut 2 og 4.
#
# c) Nullpunktene til x**2 - 144 er x = -12 og x = 12. Begge ligger utenfor
#    søkeområdet {0, 1, ..., 10}. Lars må derfor utvide søket, for eksempel
#    til x i {-15, -14, ..., 14, 15}. Da må a starte på -15, og løkka må
#    kjøre så lenge a <= 15.

def f(x):
    return x**2 - 144

a = -15
while a <= 15:
    if f(a) == 0:
        print(a)

    a = a + 1
