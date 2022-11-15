#importer la fonction random
import random

def morpionVide(tab, longueur): #crée un tableau vide
    #pour i allant de 0 a longeur 
    for i in range(longueur):
        #ajouter une liste "N" multiplié par la longueur
        tab.append([" "] * longueur)
    #pour k allant de 0 jusqu'a la longueur du tableau


def afficherMorpion(tab, longueur): #affiche le tableau
    #pour k allant de 0 jusqu'a la longueur du tableau
    for k in range(longueur): 
        #afficher le tableau
        print(tab[k])

def trouverCoord(choix):
    if choix == '1':
        x = 0
        y = 0
        return x,y
    elif choix == '2':
        x = 0
        y = 1
        return x,y
    elif choix == '3':
        x = 0
        y = 2
        return x,y
    elif choix == '4':
        x = 1
        y = 0
        return x,y
    elif choix == '5':
        x = 1
        y = 1
        return x,y
    elif choix == '6':
        x = 1
        y = 2
        return x,y
    elif choix == '7':
        x = 2
        y = 0
        return x,y
    elif choix == '8':
        x = 2
        y = 1
        return x,y
    elif choix == '9':
        x = 2
        y = 2
        return x,y
    else:
        return ValueError
    


def isWin(tab, choix, longueur):
    for k in range(longueur):
        for l in range(longueur):


'''
def premierJoueur(alea): #choisie qui est le premier joueur
    if alea == 1:
        print("tu joues en premier")  
    else:
        print("tu joues en deuxime")
'''



#initialise le score
score = [0, 0, 0]
#initalise la variable fin a False
fin = False
#initialise la liste tab vide
tab = []
morpionVide(tab, 3)
afficherMorpion(tab, 3)
#assigner a alea, un nombre entre 1 et 2
alea = random.randint(1,2)
#premierJoueur(alea)
print("tu joues les X")
#tant que jouer est egale a vrai
while fin == False:
    #assigner a choix, la chaine choisie par l'utilisateur
    choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
    x,y = trouverCoord(choix)
    while (tab[x][y] == 'X') or (tab[x][y] == 'O') or trouverCoord == ValueError:
        print("erreur: entrez un chiffre entre 1 et 9 non utilisé")
        choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
        x,y = trouverCoord(choix)
    tab[x][y] = 'X'
    print("tu as joué sur la case " + choix + "\n" )
    afficherMorpion(tab, 3)
    print("\nau tour de l'IA\n")
    #assigner a alea, un nombre entre 1 et 9
    choixCpu = str(random.randint(1,9))
    xCpu,yCpu = trouverCoord(choixCpu)
    while (tab[xCpu][yCpu] == 'X') or (tab[xCpu][yCpu] == 'O') or trouverCoord == ValueError:
        choixCpu = str(random.randint(1,9))
        xCpu,yCpu = trouverCoord(choixCpu)
    tab[xCpu][yCpu] = 'O'
    print("Le CPU a joué sur la case " + choixCpu + "\n" )
    afficherMorpion(tab, 3)
    print("\ntour suivant\n")
