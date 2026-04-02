import random

filnamn = "citat.txt"

# lägg till citat från fil
def ladda_citat():
    citat_lista = []
    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            rader = fil.readlines()
            for rad in rader:
                citat_lista.append(rad.strip())
    except FileNotFoundError:
        pass
    return citat_lista


# spara citat till fil
def spara_citat(citat_lista):
    with open(filnamn, "w", encoding="utf-8") as fil:
        for citat in citat_lista:
            fil.write(citat + "\n")


# visa alla citat
def visa_citat(citat_lista):
    if len(citat_lista) == 0:
        print("Inga citat sparade.\n")
    else:
        for i, citat in enumerate(citat_lista, 1):
            print(f"{i}. {citat}")
        print()


# lägg till citat
def lagg_till(citat_lista):
    text = input("Skriv citat: ")
    skrivare = input("Vem sa det?: ")
    nytt = f'"{text}" - {skrivare}'
    citat_lista.append(nytt)
    spara_citat(citat_lista)
    print("Citat sparat!\n")


# visa slumpmässigt citat
def slump_citat(citat_lista):
    if len(citat_lista) == 0:
        print("Inga citat att visa.\n")
    else:
        print(random.choice(citat_lista))
        print()


def main():
    citat_lista = ladda_citat()

    while True:
        print("1. Visa alla citat")
        print("2. Lägg till nytt citat")
        print("3. Visa slumpmässigt citat")
        print("4. Avsluta")

        val = input("Välj: ")

        if val == "1":
            visa_citat(citat_lista)

        elif val == "2":
            lagg_till(citat_lista)

        elif val == "3":
            slump_citat(citat_lista)

        elif val == "4":
            print("Hejdå!")
            break

        else:
            print("Fel val, försök igen.\n")


# Starta programmet
main()