#importer la fonction random
import random

def morpionVide(longueur):
    #initialise la liste coord_x vide
    coord_x = []
    #pour i allant de 0 a longeur 
    for i in range(longueur):
        #ajouter une liste "N" multiplié par la longueur
        coord_x.append(["N"] * longueur)
    #pour k allant de 0 jusqu'a la longueur du tableau
    for k in range(longueur): 
        #afficher le tableau
        print(coord_x[k])

morpionVide(3)

def afficherMorpion(coord_x, longueur):
      for k in range(longueur): 
        #afficher le tableau
        print(coord_x[k])


'''def premierJoueur(alea): #choisie qui est le premier joueur
    if alea == 1:
        print("tu joues en premier")
    else:
        print("tu joues en deuxime")
    return None


#initialise le score
score = [0, 0, 0] 
#initalise la variable fin a False
morpionVide(3)
#assigner a alea, un nombre entre 1 et 2
alea = random.randint(1,2)
#premierJoueur(alea)
#tant que jouer est egale a vrai
while fin == False:
     #assigner a choix, la chaine choisie par l'utilisateur
    choix = (input("entrez une case pour jouer (de la case 1 a la case 9)\n"))
'''