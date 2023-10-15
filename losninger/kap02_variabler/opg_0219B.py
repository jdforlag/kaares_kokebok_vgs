klokka_naa = 14
timer = 51
ankomst = (klokka_naa + timer) % 24
hele_dager = timer // 24
print(f"Vennen kommer kl {ankomst} om {hele_dager} dager.")