#importer la fonction random
import random

def elementCpu(alea): #renvoie un element aleatoire pour le CPU
    element = "ciseau"
    if alea == 1:
        element = "pierre"
    elif alea == 2:
        element = "feuille"
    return element


def result(choix, elementCpu): #renvoie le resulat du round
    #resulat pour joueur avec ciseau
    if choix == "ciseau":
        if elementCpu == "ciseau":
            return "draw"
        elif elementCpu == "feuille":
            return "win"
        else:
            return "lose"
    #resulat pour joueur avec feuille
    elif choix == "feuille":
        if elementCpu == "ciseau":
            return "lose"
        elif elementCpu == "feuille":
            return "draw"
        else:
            return "win"
    #sinon ,resulat pour joueur avec pierre
    else:
        if elementCpu == "ciseau":
            return "win"
        elif elementCpu == "feuille":
            return "lose"
        else:
            return "draw"



score = (0,0,0) #compte les victoires/defaite/egalité
jouer = True
while jouer == True:
    alea = random.randint(1,3)
    choix = str(input("entrez un element pour jouer(ciseau/pierre/feuille"))
    if result(choix, elementCpu(alea)) == "win":
        score = score + (1,0,0)
        print("victoire, bravo. ton score est de " + score)
    elif result(choix, elementCpu(alea)) == "lose":
        score = score + (0,0,1)
        print("defaite, dommage. ton score est de " + score)
    else:
        score = score + (0,1,0)
        print("egalité. ton score est de " + score)
    rejouer = str(input("souhaite tu rejouer ( envoie True pour oui et False pour non)?"))
print("partie terminé. bravo, ton score final est de " + score)