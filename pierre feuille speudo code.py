
#importer la fonction random

#faire un fonction renvoie un element aleatoire pour choisir l'element utiliser par le CPU avec comme parametre la variable alea
#initialisation de la variable element a "ciseau"
#si alea est egale a 1
    #alors changer element a "pierre"
#sinon si alea est egale a 2
    #alors changer element a "feuille"
#retourner element


#faire une fonction qui renvoie le resulat du round avec comme parametres choix et choixCPU
    #si choix est egale a "ciseau"
        #si choixCPU est egale a "ciseau"
            #retourner egalite
        #sinon si choixCPU est egale a "feuille"
            #retourner victoire
        #sinon
            #retourner perdue
    #sinon si choix est egale a "feuille"
        #si choixCPU est egale a "ciseau"
            #retourner perdue
        #sinon si choixCPU est egale a "feuille"
            #retourner egalite
        #sinon
            #retourner gagne
    #sinon
        #si choixCPU est egale a "ciseau"
            #retourner gagne
        #sinon si choixCPU est egale a "feuille"
            #retourner perdue
        #sinon
            #retourner egalite


#initialise la liste score a [0, 0, 0]
#initalise la variable pour jouer
#tant que la varaible jouer est vrai
    #alors assigner a alea, un nombre entre 1 et 3 pour le CPU
    #assigner a choix, le choix de l'element par l'utilisateur
    #si le retour de l'excecution de la fonction  result est egal a victoire
        #alors ajouter 1 au premier index de la liste score 
        #ajouter 1 au troisieme index de la liste score
        #afficher le score
    #sinon si le retour de l'excecution de la fonction  result est egal a defaite
        #ajouter 1 au deuxieme index du score 
        #afficher le score
    #sinon si le retour de l'excecution de la fonction  result est egal a egalité
        #ajouter 1 au troisieme index de la liste score
        #afficher le score
    #demander avec la fonction input() si l'utilisateur veut rejouer
#afficher le score a la fin de la partie