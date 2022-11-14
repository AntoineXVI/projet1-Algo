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
    if choix == "ciseau" or choix == "1":
        if elementCpu == "ciseau":
            return "draw"
        elif elementCpu == "feuille":
            return "win"
        else:
            return "lose"
    #resulat pour joueur avec feuille
    elif choix == "feuille" or choix == "2":
        if elementCpu == "ciseau":
            return "lose"
        elif elementCpu == "feuille":
            return "draw"
        else:
            return "win"
    #sinon ,resulat pour joueur avec pierre
    elif choix == "pierre" or choix == "3":
        if elementCpu == "ciseau":
            return "win"
        elif elementCpu == "feuille":
            return "lose"
        else:
            return "draw"
    else:
        return ValueError


#initialise le score
score = [0, 0, 0] 
jouer = True #initalise la variable pour jouer
while jouer == True:
    #assigner a alea, un nombre entre 1 et 3 pour le CPU
    alea = random.randint(1,3)
    #assigner a choix, la chaine choisie par l'utilisateur
    choix = str(input("entrez un element pour jouer(ciseau(1)/pierre(2)/feuille(3))\n"))
    if result(choix,elementCpu(alea)) == ValueError:
        print("Erreur: entrez ciseau(ou 1), feuille(ou 2) ou pierre(ou 3)\n")
        break
    elif result(choix, elementCpu(alea)) == "win":
        #ajouter 1 au premier index du score en cas de victoire
        score[0] = score[0] + 1
        print("victoire, bravo! Ton score est de : ", score )
    elif result(choix, elementCpu(alea)) == "lose":
        #ajouter 1 au deuxieme index du score en cas de defaite
        score[1] = score[1] + 1
        print("defaite, dommage. Ton score est de " , score)
    else:
        #ajouter 1 au troisieme index du score en cas d'egalite
        score[2] = score[2] + 1
        print("egalité. Ton score est de " , score)
    rejouer = str(input("souhaite tu rejouer ( envoie True si oui)\n"))
    if rejouer == "true" or rejouer == "True":
        jouer = True
    else:
        jouer = False
#afficher le score a la fin de partie
print("partie terminé. bravo, ton score final est de " , score)