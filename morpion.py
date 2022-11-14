#importer la fonction random
import random

def morpionVide(coord_x, longueur): #crée un tableau vide
    #pour i allant de 0 a longeur 
    for i in range(longueur):
        #ajouter une liste "N" multiplié par la longueur
        coord_x.append(["N"] * longueur)
    #pour k allant de 0 jusqu'a la longueur du tableau


def afficherMorpion(coord_x, longueur): #affiche le tableau
    #pour k allant de 0 jusqu'a la longueur du tableau
    for k in range(longueur): 
        #afficher le tableau
        print(coord_x[k])

'''
def premierJoueur(alea): #choisie qui est le premier joueur
    if alea == 1:
        print("tu joues en premier")  
    else:
        print("tu joues en deuxime")
'''

def changement(coord_x, choix):
    if choix == '1':
        coord_x[0][0] = 'X'
    elif choix == '2':
        coord_x[0][1] == 'X'
    elif choix == '3':
        coord_x[0][2] = 'X'
    elif choix == '4':
        coord_x[1][0] = 'X'
    elif choix == '5':
        coord_x[1][1] = 'X'
    elif choix == '6':
        coord_x[1][2] = 'X'
    elif choix == '7':
        coord_x[2][0] = 'X'
    elif choix == '8':
        coord_x[2][1] = 'X'
    elif choix == '9':
        coord_x[2][2] = 'X'
    else:
        return ValueError
    return coord_x


#initialise le score
score = [0, 0, 0]
#initalise la variable fin a False
fin = False
#initialise la liste coord_x vide
coord_x = []
morpionVide(coord_x, 3)
afficherMorpion(coord_x, 3)
#assigner a alea, un nombre entre 1 et 2
#alea = random.randint(1,2)
#premierJoueur(alea)
print("tu joues les X")
#tant que jouer est egale a vrai
while fin == False:
    #if alea == 1:
        #assigner a choix, la chaine choisie par l'utilisateur
    choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
    while changement(coord_x, choix) == ValueError:
        print("erreur: entrez un chiffre entre 1 et 9")
        choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
    coord_x = changement(coord_x, choix)
    afficherMorpion(coord_x, 3)
    print("au tour de l'IA\n")
    afficherMorpion(coord_x, 3)
    print("tour suivant\n")
