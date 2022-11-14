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


def premierJoueur(alea): #choisie qui est le premier joueur
    if alea == 1:
        print("tu joues en premier")
    else:
        print("tu joues en deuxime")


#initialise le score
score = [0, 0, 0] 
#initalise la variable fin a False
fin = False
#initialise la liste coord_x vide
coord_x = []
morpionVide(coord_x, 3)
afficherMorpion(coord_x, 3)
#assigner a alea, un nombre entre 1 et 2
alea = random.randint(1,2)
premierJoueur(alea)
#tant que jouer est egale a vrai
while fin == False:
     #assigner a choix, la chaine choisie par l'utilisateur
    choix = (input("entrez une case pour jouer (de la case 1 a la case 9)\n"))
