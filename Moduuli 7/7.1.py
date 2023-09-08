kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukausi = kuukaudet[järjestysnumero-1]
print (f"{järjestysnumero}. kuukausi on {kuukausi}.")
