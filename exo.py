'''
print("hello world")

def retournerSixPlusTrois():
    return 6 + 3

def retournerSixPlusX(x):
    return 6 + x
    

print("qui vole un " + str(retournerSixPlusX(3)) + "vole un boeuf ")

def add(x,y):
    #retourner la somme de x et y
    return x + y

def sub(x,y):
    #retourner la soustraction de x par y
    return x - y

def multiply(x,y):
    #retourner la multiplication de x et y
    return x * y

def divide(x,y):
    if y != 0 :
        #retourner la division de x par y si y n'est pas egal a 0
        return x / y
    else:
        #sinon retourner un message d'erreur car on ne divise pas par 0
        print("on divise pas par 0")
        return None

def modulo(x,y):
    if x != 0 :
        return x % y
    else:
        print("on divise pas par 0")
        return None

def CalculSalaireParSeconde(SalaireHoraire, HeureParJourOuvrable,nb_JourOuvrable):
    #Assigner a salaire annuel, le salaire par nombre d'heure travaillé par an
    salaireAnnuel =  SalaireHoraire * HeureParJourOuvrable * nb_JourOuvrable
    #Calculer, puis assigner a nombreParSecondeParAn , le nombre de seconde dans une année non bisextile
    nombreDeSecondeParAn = 60 * 60 * 24 *365
    #retourner le salaire Annuel divisé par le nombre de seconde par An
    return salaireAnnuel / nombreDeSecondeParAn

def CalculSalaireNet(salaireBrut, coeff):
    #Calculer puis Assigner a taxe, le montant des taxes a retirer
    taxe = salaireBrut * (coeff / 100)
    #retourner le salaire net final
    return salaireBrut - taxe


def CalculSalaire(SalaireBrut, public):
    #si j'occupe un poste de la fonction publique
    if public:
        #alors je retourne le salaire brut -15% de taxe
        return CalculSalaireNet(SalaireBrut, 15)
    #sinon, c'est que je travaille dans le secteur privé
    else:
        #alors je retourne le salaire brut -23% de taxes
        return CalculSalaireNet(SalaireBrut, 23)

def minigame(lettreChoisie):
    #asssigner a lettre, une lettre aleatoire avec la fonction input()
    lettre = input()
    #choissir une autre lettre et reessayer tant que la lettre est mauvaise
    while lettre != lettreChoisie :
        print("mauvais caractere")
        lettre = input()
    #ecrire un message quand la lettre est la bonne 
    print("bravo")
    return None


tableau = [1,25,24,36,41,1,897]

#pour recuperer la valeur 36, je prends dans le tableau l'index 3
print(tableau[3]) #affiche 36

len(tableau) #renvoie la longueur du tableau

nom = "pichard "
prenom = "antoine "
identite = nom + prenom #renvoie "pichard antoine "
'''

'''ex1 
faire une fonction qui concatene 2 chaines de caract, les separants par des virgules

ex2
faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere avec
l'ensemble des occurences d'un chiffre ex.general:
pour tableau = [0,1,1,1,0,1,1,0,1]
la fonction(tableau, 0) doit renvoyer "0, 4, 7". n'hesitez pas a implementer la premiere fonction'''

def concat(phrase1, phrase2): #renvoie une chaine concatené a partir de 2 chaines
    #assigner a phraseConcat la concatenation des 2 chaines séparé par une virgule
    phraseConcat = str(phrase1) + ", " + str(phrase2)
    #renvoie la phrase concatené
    return phraseConcat 

def chaineOcuurences(tableau, occurence): #renvoie une chaine str avec toute les occurences choisie
    #initailisation de la chaine 
    phrase = ""
    #initialiser isFirst a True
    isFirst = True
    #tester toutes les occurences du tableau avec une boucle  
    for k in range(len(tableau)):
        #si l'occurence choisie est egale a l'element du tableau
        if occurence == tableau[k]:
            if isFirst == True:
                ##assigner a chainerRetour la valeur de i
                phrase = k
                #changer isFirst a faux
                isFirst = False
            else:
                #alors on le concatene avec la phrase qui liste les index du tableau
                phrase = concat(phrase, k)
    #retourner la phrase complete
    return phrase

print(chaineOcuurences([0, 0, 1, 2, 3, 0], 0)) #renvoie "0, 1, 5"

def findIndexes(tableau, x): #renvoie une chaine str avec toute les occurences choisie
    #initialiser i a 0
    i = 0
    #initialiser isFirst a True
    isFirst = True
    #initialiser chaine retour a une chaine str vide
    chaineRetour = ""
    #tant que i est plus petit que le retour de l'excecution de la fonction len avec comme parametre tableau
    while i < len(tableau):
        #assigner a selected la valeur du tabeau d'indice i 
        selected = tableau[i]
        #si selected est egale a l'occurence recherché
        if selected == x:
            #si selected est la premeiere valeur
            if isFirst == True:
                ##assigner a chainerRetour la valeur de i
                chaineRetour = i
                #changer isFirst a faux
                isFirst = False
            else:
                #assigner a chaineRetour, la concatenation de la chaineRetour et de l'indice i grace a la fonction concat deja crée
                chaineRetour = concat(chaineRetour, i)
        #incrementer i
        i = i + 1
    #retourner la chaine avec la liste d'occurences complete
    return chaineRetour

#print(findIndexes([0, 0, 1, 2, 3, 0], 0))

def Fibo(x,xmax): #renvoie une chaine de la suite de fibonacci jusqu'a la valeur xmax atteinte, avec une valeur choisie en parametre
    #initialiser la chaine a "0"
    chaineFibo = [0, x]
    #initialiser i a 0
    i = 1
    #tant que x est inferieur a la valeur xmax choisie
    while i <= xmax:
        #alors on ajoute a la liste le dernier et l'avant dernier terme de la liste
        chaineFibo.append(chaineFibo[i] + chaineFibo[i - 1])
        #on incremente i
        i = i + 1
    return chaineFibo


print(Fibo(5, 10))