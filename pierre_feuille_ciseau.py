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


#initialise le score
score = [0, 0, 0] 
jouer = True #initalise la variable pour jouer
while jouer == True:
    #assigner a alea, un nombre entre 1 et 3 pour le CPU
    alea = random.randint(1,3)
    #assigner a choix, la chaine choisie par l'utilisateur
    choix = str(input("entrez un element pour jouer(ciseau/pierre/feuille)p"))
    if result(choix, elementCpu(alea)) == "win":
        #ajouter 1 au premier index du score en cas de victoire
        score[0] = score[0] + 1
        print("victoire, bravo. ton score est de : " , score)
    elif result(choix, elementCpu(alea)) == "lose":
        #ajouter 1 au deuxieme index du score en cas de defaite
        score[1] = score[1] + 1
        print("defaite, dommage. ton score est de " , score)
    else:
        #ajouter 1 au troisieme index du score en cas d'egalite
        score[2] = score[2] + 1
        print("egalité. ton score est de " , score)
    jouer = str(input("souhaite tu rejouer ( envoie True pour oui et False pour non)?"))
#afficher le score a la fin de partie
print("partie terminé. bravo, ton score final est de " , score)