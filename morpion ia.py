#importer la fonction random
import random

def morpionVide(tab, longueur): #crée un tableau vide
    #pour i allant de 0 a longeur 
    for i in range(longueur):
        #ajouter une liste " " multiplié par la longueur
        tab.append([" "] * longueur)
    #pour k allant de 0 jusqu'a la longueur du tableau


def afficherMorpion(tab, longueur): #affiche le tableau
    #pour k allant de 0 jusqu'a la longueur du tableau
    for k in range(longueur): 
        #afficher le tableau
        print('|'.join(str(e) for e in tab[k]))

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
    if tab[0][0] == tab[xChoix][yChoix] and tab[1][1] == tab[xChoix][yChoix] and tab[2][2] == tab[xChoix][yChoix]:
            return tab[xChoix][yChoix]
    elif tab[0][2] == tab[xChoix][yChoix] and tab[1][1] == tab[xChoix][yChoix] and tab[2][0] == tab[xChoix][yChoix]:
            return tab[xChoix][yChoix]


def cpuBlock(tab): #fonction qui permet de savoir si le joueur a deux X aligné et retourne la case joué si oui, ou sinon retourne "NON"
    #test cases impairs
    if (tab[2][0] == 'X' and tab[0][2] == 'X' or tab[0][0] == 'X' and tab[2][2] == 'X' or tab[1][0] == 'X' and tab[1][2] == 'X' or tab[2][1] == 'X' and tab[1][2] == 'X') and tab[1][1] == ' ':
        return '5'
    elif (tab[1][1] == 'X' and tab[2][2] == 'X' or tab[0][1] == 'X' and tab[0][2] == 'X' or tab[1][0] == 'X' and tab[2][0] == 'X') and tab[0][0] == ' ':
        return '1'
    elif (tab[1][1] == 'X' and tab[2][0] == 'X' or tab[0][0] == 'X' and tab[0][1] == 'X' or tab[1][2] == 'X' and tab[2][2] == 'X') and tab[0][2] == ' ':
        return '3'
    elif (tab[1][1] == 'X' and tab[0][2]== 'X' or tab[2][1] == 'X' and tab[2][2] == 'X' or tab[0][0] == 'X' and tab[1][0] == 'X') and tab[2][0] == ' ':
        return '7'
    elif (tab[1][1] == 'X' and tab[0][0]== 'X' or tab[2][0] == 'X' and tab[2][1] == 'X' or tab[0][2] == 'X' and tab[1][2] == 'X') and tab[2][2] == ' ':
        return '9'
    #test cases pairs
    elif (tab[0][0] == 'X' and tab[0][2] == 'X' or tab[1][1] == 'X' and tab[2][1] == 'X') and tab[0][1] == ' ':
        return '2'
    elif (tab[1][1] == 'X' and tab[1][2] == 'X' or tab[2][0] == 'X' and tab[0][0] == 'X') and tab[1][0] == ' ':
        return '4'
    elif (tab[1][0] == 'X' and tab[1][1] == 'X' or tab[2][2] == 'X' and tab[0][2] == 'X') and tab[1][2] == ' ':
        return '6'
    elif (tab[2][0] == 'X' and tab[2][2] == 'X' or tab[0][1] == 'X' and tab[1][1] == 'X') and tab[2][1] == ' ':
        return '8'
    else:
        return "NON"

def cpuWin(tab): #fonction qui permet de savoir si le joueur a deux X aligné et retourne la case joué si oui, ou sinon retourne "NON"
    #test cases impairs
    if (tab[2][0] == 'O' and tab[0][2] == 'O' or tab[0][0] == 'O' and tab[2][2] == 'O' or tab[1][0] == 'O' and tab[1][2] == 'O' or tab[2][1] == 'O' and tab[1][2] == 'O') and tab[1][1] == ' ':
        return '5'
    elif (tab[1][1] == 'O' and tab[2][2] == 'O' or tab[0][1] == 'O' and tab[0][2] == 'O' or tab[1][0] == 'O' and tab[2][0] == 'O') and tab[0][0] == ' ':
        return '1'
    elif (tab[1][1] == 'O' and tab[2][0] == 'O' or tab[0][0] == 'O' and tab[0][1] == 'O' or tab[1][2] == 'O' and tab[2][2] == 'O') and tab[0][2] == ' ':
        return '3'
    elif (tab[1][1] == 'O' and tab[0][2]== 'O' or tab[2][1] == 'O' and tab[2][2] == 'O' or tab[0][0] == 'O' and tab[1][0] == 'O') and tab[2][0] == ' ':
        return '7'
    elif (tab[1][1] == 'O' and tab[0][0]== 'O' or tab[2][0] == 'O' and tab[2][1] == 'O' or tab[0][2] == 'O' and tab[1][2] == 'O') and tab[2][2] == ' ':
        return '9'
    #test cases pairs
    elif (tab[0][0] == 'O' and tab[0][2] == 'O' or tab[1][1] == 'O' and tab[2][1] == 'O') and tab[0][1] == ' ':
        return '2'
    elif (tab[1][1] == 'O' and tab[1][2] == 'O' or tab[2][0] == 'O' and tab[0][0] == 'O') and tab[1][0] == ' ':
        return '4'
    elif (tab[1][0] == 'O' and tab[1][1] == 'O' or tab[2][2] == 'O' and tab[0][2] == 'O') and tab[1][2] == ' ':
        return '6'
    elif (tab[2][0] == 'O' and tab[2][2] == 'O' or tab[0][1] == 'O' and tab[1][1] == 'O') and tab[2][1] == ' ':
        return '8'
    else:
        return "NON"

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
#initialise la liste tabvide
tab= []
morpionVide(tab, 3)
afficherMorpion(tab, 3)
#assigner a alea, un nombre entre 1 et 2
alea = random.randint(1,2)
if alea == 1:
    print("tu joues en premier\n")
else:
    print("tu joues en deuxieme\n")
    isFirst = False
    cpuFirst = True
print("tu joues les X\n") 

#tant que WinCpu et winUser sont egaux a faux
while winCpu == False and winUser == False:
    if isFirst == True:
        countTour = countTour + 1 
        print("à ton tour - Tour numero " + str(countTour) + "\n")
        #assigner a choix, la chaine choisie par l'utilisateur 
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

    if cpuFirst == True or (countTour == 1 and tab[1][1] == 'X'): #si le cpu commence ou joue en deuxieme et le joueur vient de jouer au milieu
        countTour = countTour + 1
        print("au tour de l'IA - Tour numero " + str(countTour) + "\n")
        #assigner a choixCpu, un nombre entre 1 et 9
        choixCpu = str(random.randint(1,9))
        x,y = trouverCoord(choixCpu)
        #jouer sur un des 4 coins
        while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
            choixCpu = str(random.randint(1,9))
            x,y = trouverCoord(choixCpu)
        tab[x][y] = 'O'
        print("Le CPU a joué sur la case " + choixCpu + "\n" )
        afficherMorpion(tab, 3)
        cpuFirst = False
    else: #sinon
        countTour = countTour + 1
        print("au tour de l'IA - Tour numero " + str(countTour) + "\n")
        if cpuWin(tab) != "NON": #si le CPU a 2 ronds alignés
            choixCpu = cpuWin(tab)
            x,y = trouverCoord(choixCpu)
            tab[x][y] = 'O'
            print("Le CPU a joué sur la case " + choixCpu + "\n" )
            afficherMorpion(tab, 3)
        elif cpuBlock(tab) != "NON": #si le joueur a 2 croix alignés
            choixCpu = cpuBlock(tab)
            x,y = trouverCoord(choixCpu)
            tab[x][y] = 'O'
            print("Le CPU a joué sur la case " + choixCpu + "\n" )
            afficherMorpion(tab, 3)
        else: #sinon
            if tab[1][1] != 'X':    #si X ne joue pas au milieu
                if countTour == 2 or countTour == 5: #si X ne joue pas au milieu au deuxieme cinquieme tour
                    tab[1][1] = 'O'
                    print("Le CPU a joué sur la case 5\n" )
                    afficherMorpion(tab, 3)
                elif countTour == 3: #si X ne joue pas au milieu au troisieme tour
                    choixCpu = str(random.randint(1,9))
                    x,y = trouverCoord(choixCpu)
                    while tab[x][y] != 'O' :
                        choixCpu = str(random.randint(1,9))
                        x,y = trouverCoord(choixCpu)
                    if x == 0 and y == 0:
                        if tab[0][1] == 'X':
                            choixCpu = str(random.choice([7,9]))
                            x,y = trouverCoord(choixCpu)   
                        elif tab[1][0] == 'X':
                            choixCpu = str(random.choice([1,9]))
                            x,y = trouverCoord(choixCpu)
                        else:
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                            while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
                                choixCpu = str(random.randint(1,9))
                                x,y = trouverCoord(choixCpu)
                                if (tab[x][y] != 'X' and tab[x][y] != 'O'):
                                    break
                    elif x == 2 and y == 0:
                        if tab[2][1] == 'X':
                            choixCpu = str(random.choice([1,3]))
                            x,y = trouverCoord(choixCpu)
                        elif tab[1][0] == 'X':
                            choixCpu = str(random.choice([3,9]))
                            x,y = trouverCoord(choixCpu)
                        else:
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                            while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
                                choixCpu = str(random.randint(1,9))
                                x,y = trouverCoord(choixCpu)
                                if (tab[x][y] != 'X' and tab[x][y] != 'O'):
                                    break
                    elif x == 0 and y == 2:
                        if tab[0][1] == 'X':
                            choixCpu = str(random.choice([7,9]))
                            x,y = trouverCoord(choixCpu)
                        elif tab[1][2] == 'X':
                            choixCpu = str(random.choice([1,7]))
                            x,y = trouverCoord(choixCpu)
                        else:
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                            while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
                                choixCpu = str(random.randint(1,9))
                                x,y = trouverCoord(choixCpu)
                                if (tab[x][y] != 'X' and tab[x][y] != 'O'):
                                    break
                    elif x == 2 and y == 2:
                        if tab[2][1] == 'X':
                            choixCpu = str(random.choice([1,3]))
                            x,y = trouverCoord(choixCpu)                            
                        elif tab[1][2] == 'X':
                            choixCpu = str(random.choice([1,7]))
                            x,y = trouverCoord(choixCpu)  
                        else:
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                            while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
                                choixCpu = str(random.randint(1,9))
                                x,y = trouverCoord(choixCpu)
                                if (tab[x][y] != 'X' and tab[x][y] != 'O'):
                                    break
                    else:
                        choixCpu = str(random.randint(1,9))
                        x,y = trouverCoord(choixCpu)
                        while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                            if (tab[x][y] != 'X' and tab[x][y] != 'O'):
                                break
                    tab[x][y] = 'O'
                    print("Le CPU a joué sur la case " + choixCpu + "\n" )
                    afficherMorpion(tab, 3)       
                else: #sinon = si 'x' ne joue pas au milieu au 2/3/5 eme tour
                    if tab[x][y] == 'X':
                        choixCpu = str(random.randint(1,9))
                        x,y = trouverCoord(choixCpu)
                        while (trouverCoord(choixCpu) != (0, 0)) and (trouverCoord(choixCpu) != (0, 2)) and (trouverCoord(choixCpu) != (2, 0)) and (trouverCoord(choixCpu) != (2, 2)):
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                        tab[x][y] = 'O'
                    else: 
                        choixCpu = str(random.randint(1,9))
                        x,y = trouverCoord(choixCpu)
                        while (tab[x][y] == 'X') and (tab[x][y] == 'O') or trouverCoord == ValueError:
                            choixCpu = str(random.randint(1,9))
                            x,y = trouverCoord(choixCpu)
                        tab[x][y] = 'O'
                    print("Le CPU a joué sur la case " + choixCpu + "\n" )
                    afficherMorpion(tab, 3)
            elif tab[1][1] == 'X': #si X joue au milieu 
                if  countTour == 3: #si X joue au milieu au 3eme tour
                    x,y = trouverCoord(str(10 - int(choixCpu))) #jouer sur le coin opposé
                    tab[x][y] = 'O'
                    print("Le CPU a joué sur la case " + (str(10 - int(choixCpu))) + "\n" )
                    afficherMorpion(tab, 3)
                else:
                    choixCpu = str(random.randint(1,9))
                    x,y = trouverCoord(choixCpu)
                    while (tab[x][y] == 'X') and (tab[x][y] == 'O') or trouverCoord == ValueError:
                        choixCpu = str(random.randint(1,9))
                        x,y = trouverCoord(choixCpu)
                    tab[x][y] = 'O'
                    print("Le CPU a joué sur la case " + choixCpu + "\n" )
                    afficherMorpion(tab, 3)
    if isWin(tab, x, y) == 'O': #si cpu a 3 ronds aligné
        winCpu == True
        print("Dommage, tu as perdu\n")
        break
    else:
        if countTour >= 9: #si le nombre de tours supérieur a 9 = plateau rempli
            print("Egalité.\n")
            break
        print("Fin du tour\n")
print("Fin de Partie\n")         