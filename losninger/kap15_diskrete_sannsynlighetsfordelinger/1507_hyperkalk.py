import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import hypergeom
#plt.rcParams['font.size'] = 14
# Initialiser variabler
n = 10  # Totalt antall tall
m = 4   # Antall vinnertall
r = 6   # Antall tall spilleren velger

# Forbered liste for sannsynligheter og x-verdier
p_verdier = []
x_verdier = list(range(0, m+1))  # Antall riktige tall spilleren kan ha

# Beregn sannsynligheter og legg dem til i listen
for x in x_verdier:
    sanns = hypergeom.pmf(x, n, m, r)
    print(f"P(X={x}) = {sanns:.3f}")
    p_verdier.append(sanns)

# Lagre kumulative sannsynligheter
p_kumverdier = []
for x in x_verdier:
    kum_sanns = hypergeom.cdf(x, n, m, r)
    p_kumverdier.append(kum_sanns)

# Tegne sannsynlighetsfordelingen
plt.figure(figsize=(12, 4))  # Angi størrelsen på hele figurvinduet
plt.subplot(1, 2, 1)  # Forbered første delplot
plt.ylim(0, 1.1)
plt.bar(x_verdier, p_verdier)  # Stolpediagram for sannsynligheter

plt.title('Sannsynlighetsfordeling')
plt.xlabel('Antall vinnertall')
plt.ylabel(r'$P(X=x)$')

# Tegne kumulative sannsynligheter
plt.subplot(1, 2, 2)  # Forbered andre delplot
plt.ylim(0, 1.1)
plt.bar(x_verdier, p_kumverdier)  # Stolpediagram for kumulative sannsynligheter
plt.title('Kumulativ sannsynlighetsfordeling')
plt.xlabel('Antall vinnertall')
plt.ylabel(r'$P(X\leq x)$')

plt.tight_layout()  # Sikrer at alt passer innenfor figurrammen
#plt.savefig('kumhyper2figs.pdf', dpi=400, bbox_inches='tight', pad_inches = 0)

plt.show()  # Viser figuren

