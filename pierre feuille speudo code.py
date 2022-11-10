
#importer la fonction random

#faire un fonction elementCpu qui renvoie une chaine element avec comme parametre la variable alea
#initialisation de la variable element a "ciseau"
#si alea est egale a 1
    #alors changer element a "pierre"
#sinon si alea est egale a 2
    #alors changer element a "feuille"
#retourner element


#faire une fonction result qui renvoie le resulat du round avec comme parametres choix et choixCPU
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
#initalise la variable jouer a True
#tant que la variable jouer est vrai
    #alors assigner a alea, le retour de l'excecution de la fonction random, avec parametre 1 et 3 
    #assigner a choix, le str du retour de l'excecution de la fonction input , avec comme parametre "entrez un element pour jouer(ciseau/pierre/feuille)"
    #si le retour de l'excecution de la fonction result avec comme parametre choix et elementCpu(alea) est egal a victoire
        #alors ajouter 1 au premier index de la liste score 
        #ajouter 1 au troisieme index de la liste score
        #afficher le score
    #sinon si le retour de l'excecution de la fonction result avec comme parametre choix et elementCpu(alea) est egal a defaite
        #ajouter 1 au deuxieme index du score 
        #afficher le score
    #sinon si le retour de l'excecution de la fonction result avec comme parametre choix et elementCpu(alea) est egal a egalité
        #ajouter 1 au troisieme index de la liste score
        #afficher le score
    #changer la variable jouer, au str du retour de l'excecution de la fonction input , avec comme parametre "souhaite tu rejouer ( envoie True(oui) ou False(non)?"
#afficher le score a la fin de la partie