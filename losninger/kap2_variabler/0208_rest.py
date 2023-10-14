boller = 4
venner = 9
per_venn = boller // venner
rest = boller % venner
print(f"{per_venn} boller per venn")
print(f"De {rest} siste bollene kan deles opp...")

ekstrabiter = 8*rest
ekstrabiter_per_venn = ekstrabiter // venner
rest_ekstrabiter = ekstrabiter % venner

print(f"{ekstrabiter_per_venn} ekstra bollebiter per venn")
print(f"{rest_ekstrabiter} ekstra bollebiter til overs.")