
etunimi = input("Anna etuimesi: ")
syntymävuosi = int(input("Syötä syntymävuotesi: "))

ikä = 2023-syntymävuosi

jakojäännös = ikä%10
jäljellä = 10-jakojäännös
pyöreitä_juhlittu = ikä//10

print("Juhlit pyöreitä vuosia "+ str(jäljellä)+" vuoden päästä. Täytät silloin "+ str(ikä) + " vuotta")
