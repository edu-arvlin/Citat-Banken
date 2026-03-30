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


