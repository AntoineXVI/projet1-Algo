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
    


def isWin(tab, xChoix, yChoix):
    #test en ligne
    if yChoix == 0:
        if (tab[xChoix][yChoix + 1] == tab[xChoix][yChoix])and (tab[xChoix][yChoix + 2] == tab[xChoix][yChoix]) :
            return tab[xChoix][yChoix]
    elif yChoix == 1:
        if (tab[xChoix][yChoix - 1] == tab[xChoix][yChoix])and (tab[xChoix][yChoix + 1] == tab[xChoix][yChoix]) :
            return tab[xChoix][yChoix]
    elif yChoix == 2:
        if (tab[xChoix][yChoix - 2] == tab[xChoix][yChoix])and (tab[xChoix][yChoix - 1] == tab[xChoix][yChoix]) :
            return tab[xChoix][yChoix]
    #test en colonne 
    if xChoix == 0:
        if (tab[xChoix + 1][yChoix] == tab[xChoix][yChoix])and (tab[xChoix + 2][yChoix] == tab[xChoix][yChoix]) :
            return tab[xChoix][yChoix]
    elif xChoix == 1:
        if (tab[xChoix - 1][yChoix ] == tab[xChoix][yChoix])and (tab[xChoix  + 1][yChoix] == tab[xChoix][yChoix]) :
            return tab[xChoix][yChoix]
    elif xChoix == 2:
        if (tab[xChoix - 2][yChoix] == tab[xChoix][yChoix])and (tab[xChoix - 1][yChoix] == tab[xChoix][yChoix]) :
            return tab[xChoix][yChoix]
    #test en diagonale
    if xChoix == 1 and yChoix == 1:
        if tab[0][0] == tab[xChoix][yChoix] and tab[2][2] == tab[1][1]:
            return tab[xChoix][yChoix]
        elif tab[0][2] == tab[xChoix][yChoix] and tab[2][0] == tab[1][1]:
            return tab[xChoix][yChoix]



#initalise la variable WinCpu a False
winCpu = False
#initalise la variable winUser a False
winUser = False
#initalise la variable isFirst a True
isFirst = True
#initalise la variable cpuFirst a False
cpuFirst = False
#initalise la variable countTour a 0
countTour = 0
#initialise la liste tab vide
tab = []
morpionVide(tab, 3)
afficherMorpion(tab, 3)
#assigner a alea, un nombre entre 1 et 2
alea = random.randint(1,2)
if alea == 1:
    print("tu joues en premier\n")
else:
    print("tu joues en deuxime\n")
    isFirst = False
    cpuFirst = True
print("tu joues les X\n") 

#tant que WinCpu et winUser sont egaux a faux
while winCpu == False and winUser == False:
    if isFirst == True:
        #assigner a choix, la chaine choisie par l'utilisateur
        print("à ton tour\n")
        choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
        while trouverCoord(choix) == ValueError:
            print("erreur: entrez un caractere numerique entre 1 et 9")
            choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
        x,y = trouverCoord(choix)
        while (tab[x][y] == 'X') or (tab[x][y] == 'O') or trouverCoord(choix) == ValueError:
            print("erreur: entrez un chiffre entre 1 et 9 non utilisé")
            choix = str(input("entrez une case (de la case 1 a la case 9)\n"))
            x,y = trouverCoord(choix)
        tab[x][y] = 'X'
        print("tu as joué sur la case " + choix + "\n" )
        afficherMorpion(tab, 3)
        countTour = countTour + 1
        if isWin(tab, x, y) == 'X':
            winUser == True
            print("Bravo, tu as gagné\n")
            break
        else:
            if countTour >= 9:
                print("Egalité.\n")
                break
    else:
        isFirst = True

    if cpuFirst == True:
        print("au tour de l'IA\n")
        #assigner a alea, un nombre entre 1 et 9
        choixCpu = str(random.randint(1,9))
        x,y = trouverCoord(choixCpu)
        while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
            choixCpu = str(random.randint(1,9))
            x,y = trouverCoord(choixCpu)
        tab[x][y] = 'O'
        print("Le CPU a joué sur la case " + choixCpu + "\n" )
        afficherMorpion(tab, 3)
        countTour = countTour + 1
    else:
        isFirst = False

    #assigner a alea, un nombre entre 1 et 9
    choixCpu = str(random.randint(1,9))
    x,y = trouverCoord(choixCpu)
    while (tab[x][y] == 'X') or (tab[x][y] == 'O') or trouverCoord == ValueError:
        choixCpu = str(random.randint(1,9))
        x,y = trouverCoord(choixCpu)
    tab[x][y] = 'O'
    print("Le CPU a joué sur la case " + choixCpu + "\n" )
    afficherMorpion(tab, 3)
    countTour = countTour + 1
    if isWin(tab, x, y) == 'O':
        winCpu == True
        print("Dommage, tu as perdu\n")
        break
    else:
        if countTour >= 9:
            print("Egalité.\n")
            break
        print("Fin du tour numero " + str(countTour) + ":\n")
print("Fin de Partie\n")
