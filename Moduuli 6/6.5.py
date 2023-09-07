def poista_parittomat(lista):
    parilliset = [luku for luku in lista if luku % 2== 0]
    return parilliset

if __name__ == "__main__":
    numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    alkuperainen = numerot
    karsittu = poista_parittomat(numerot)

    print("Alkuperäinen lista:", alkuperainen)
    print("Karsittu lista (parilliset):", karsittu)
