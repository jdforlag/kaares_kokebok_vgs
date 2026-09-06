# Feilene i koden var:
#   1) send_tilbake er ikke Python. Nøkkelordet heter return
#   2) Variabelen het delta_x, men ble brukt som dx lenger nede
#   3) Bredden skal være 1, ikke 0,5, siden [0, 2] deles i to intervaller
#   4) Høyden til det andre rektanglet er f(1), ikke f(-1)
#   5) Arealene skal legges sammen, ikke multipliseres
#   6) I en f-streng brukes krøllparenteser, ikke hakeparenteser

def f(x):
    return -2*x + 4

dx = 1
R1 = dx*f(0)
R2 = dx*f(1)
samlet_areal = R1 + R2
print(f"Rektangelsummen er {samlet_areal}.")
