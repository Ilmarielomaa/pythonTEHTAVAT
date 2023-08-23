sukupuoli = input("mies vai nainen: ")
hemoglobiini = int(input("Syötä hemoglobiini arvosi: "))

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini arvosi ovat alhaiset. ")
    elif hemoglobiini > 195:
        print("hemoglobiiniarvosi ovat korkealla. ")
    else:
        print("hemoglobiini arvosi ovat normaalit. ")

elif sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("hemoglobiini arvosi ovat alhaiset. ")
    elif hemoglobiini > 175:
        print("hemoglobiini arvosi ovat korkealla. ")
    else:
        print/"hemoglobiini arvosi ovat normaalit. "
