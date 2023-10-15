boller = 22
venner = 9
per_venn = boller // venner
rest = boller % venner
print(f"{per_venn} hele boller per venn")
print(f"De {rest} siste bollene kan deles opp...")

ekstrabiter = 8*rest
ekstrabiter_per_venn = ekstrabiter // venner
rest_ekstrabiter = ekstrabiter % venner
print(f"{ekstrabiter_per_venn} ekstrabiter per venn")
print(f"De {rest_ekstrabiter} siste ekstrabitene kan deles opp...")
