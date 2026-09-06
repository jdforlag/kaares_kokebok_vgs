from tabulate import tabulate
import numpy as np

x_verdier = np.arange(10, 110, 10)  # [10, 20, ..., 100]
lg_x = np.log10(x_verdier)
ln_x = np.log(x_verdier)
forhold = ln_x / lg_x  # Den nye kolonnen

tabell_data = zip(x_verdier, lg_x, ln_x, forhold)
overskrifter = ["x", "lg(x)", "ln(x)", "ln(x) / lg(x)"]
tabell = tabulate(tabell_data, headers=overskrifter)
print(tabell)

# Forklaring:
# Den siste kolonnen er den samme uansett hvilken x vi velger, nemlig
# ln(10) = 2.30259. Altså er   ln(x) / lg(x) = ln(10),   og da får vi
#     lg(x) = ln(x) / ln(10)
print(f"{np.log(10) = }")
