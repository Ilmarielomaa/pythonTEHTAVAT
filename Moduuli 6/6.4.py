def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

if __name__== "__main__":
    numerot = [1, 2, 3, 4, 5]
    tulos = laske_summa(numerot)
    print(f"Listan summa on: {tulos}")