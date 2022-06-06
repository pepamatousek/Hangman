import os
from random import choice

from figurine import hangman
from words import random_words as slova

hrajeme = True
uhadnuta_pismena = set()
chybna_pismena = list("")
chybna_slova = list("")

# inicializace hry
while hrajeme:
    
    # zajištění neopakování se slov
    if len(slova) != 0:
        slovo = choice(slova)
        slova.remove(slovo)

    # když dojdou slova
    elif len(slova) == 0:
        print("Dosla slova")
        exit()

    tajenka = ["_"] * len(slovo)
    zivoty = 7
    hra_bezi = True

    # index zaveden kvůli prodlužování řádku
    i = ""

    # cyklus pro hru
    while hra_bezi and zivoty != 0:
        os.system("cls")
        print(f"Životy: {zivoty} 💗")
        print(f"Tajenka: {' '.join(tajenka)}")
        print(hangman[7 - zivoty])

        if len(chybna_pismena) != 0:
            print("-" * ((len(chybna_pismena) * 3) + 17))
            print("Nesprávná písmena:",", ".join(chybna_pismena))
            print("-" * ((len(chybna_pismena) * 3) + 17))

        # vykreslení čar a výpis chybně hádaných slov
        if len(chybna_slova) != 0:
            
            # ošetření délky čar
            if len(hadani) != 1 and hadani != slovo:
                i += hadani

            # vykreslení čar a výpis chybně hádaných slov
            print("-" * (len(i) + (len(chybna_slova) * 2) + 16))
            print("Nesprávná slova:",", ".join(chybna_slova))
            print("-" * (len(i) + (len(chybna_slova) * 2) + 16))

        hadani = input("Hadej písmeno nebo slovo: ")
        
        if hadani in uhadnuta_pismena:
            chybna_pismena.append(hadani)

        # uhald slovo?
        if hadani == slovo:
            os.system("cls")
            print(f"Životy: {zivoty} 💗")
            print(f"Tajenka: {' '.join(hadani)}")
            print(hangman[7 - zivoty])
            print(f"⭐ Vyhrál/a jsi, gratulujeme! ⭐", "", sep="\n")
            break

        # uhodl hráč písmeno?
        elif len(hadani) == 1 and hadani in slovo and hadani not in uhadnuta_pismena:

            # pridat pismeno do tajenky
            for index, pismeno in enumerate(slovo):
                if pismeno == hadani:
                    tajenka[index] = hadani
                    uhadnuta_pismena.add(hadani)

            
            # je v tajence jeste nejake pismeno k doplneni?
            if "_" not in tajenka:
                os.system("cls")
                print(f"Životy: {zivoty} 💗")
                print(f"Tajenka: {' '.join(tajenka)}")
                print(hangman[7 - zivoty])
                print(f"⭐ Vyhrál/a jsi, gratulujeme! ⭐", "", sep="\n")
                hra_bezi = False
        
        else:
            # když hráč neuhodne písmeno
            if len(hadani) == 1 and hadani not in slovo:
                chybna_pismena.append(hadani)
                zivoty -= 1

            # když hráč neuhodne slovo
            elif len(hadani) > 1 and hadani != slovo:
                chybna_slova.append(hadani)
                zivoty -= 1
            
            # ostatní případy nezdaru (když je písmeno již v tajence)
            else:    
                zivoty -= 1
    else:
        # když dojdou hráči životy
        if zivoty == 0:
            os.system("cls")
            print(f"Životy: {zivoty} 💗")
            print(f"Tajenka: {' '.join(tajenka)}")
            print(hangman[7 - zivoty])
            print(f"Prohráls 💀 🙁 Snad příště...", f"Hledané slovo: *{slovo}*", sep="\n")

    # konec hry - hráčovo rozhodnutí
    dalsi_hra = input("Chceš hrát další hru? [a/n]: ")
    
    # konec hry - když zadá hráč "a", že chce pokračovat
    if dalsi_hra == "a":
        uhadnuta_pismena.clear()
        chybna_pismena.clear()
        chybna_slova.clear()
        continue

    # konec hry - když zadá hráč "n", že nechce pokračovat
    elif dalsi_hra == "n":
        break

    # konec hry - když zadá hráč něco jiného
    else:
        break

