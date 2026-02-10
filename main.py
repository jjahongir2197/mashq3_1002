class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

def jami_hisob(savat):
    total = 0
    for mahsulot in savat:
        total += mahsulot.narx
    return total

savat = []

while True:
    print("\n1. Mahsulot qo'shish")
    print("2. Savatni ko'rish")
    print("3. Jami narx")
    print("4. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        nom = input("Mahsulot nomi: ")
        narx = int(input("Narxi: "))
        savat.append(Mahsulot(nom, narx))
        print("Mahsulot qo'shildi.")
    elif tanlov == "2":
        print("\n--- SAVAT ---")
        for m in savat:
            print(f"{m.nom} - {m.narx} so'm")
    elif tanlov == "3":
        print(f"Jami: {jami_hisob(savat)} so'm")
    elif tanlov == "4":
        print("Chiqildi.")
        break
    else:
        print("Xato tanlov!")
