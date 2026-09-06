# Feilene i koden var:
#   1) Biblioteket heter matplotlib.pyplot, ikke matplotlib.pythonplot
#   2) Kallenavnet må være plt, siden koden bruker plt lenger nede
#   3) y-verdiene manglet en klammeparentes, og innholdet var tekst
#      i stedet for tallene 2, 5 og 6
#   4) Argumentene i plt.plot skilles med komma, ikke kolon
#   5) Kommandoen for å vise diagrammet heter show, ikke show_off

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 5, 6]
plt.plot(x, y)
plt.show()
