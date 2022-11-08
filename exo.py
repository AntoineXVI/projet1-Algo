print("hello world")

def retournerSixPlusTrois():
    return 6 + 3

def retournerSixPlusX(x):
    return 6 + x
    

print("qui vole un " + retournerSixPlusX(3) + "vole un boeuf ")

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

'''ex1 
faire une fonction qui concatene 2 chaines de caract, les separants par des virgules

ex2
faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere avec
l'ensemble des occurences d'un chiffre ex.general:
pour tableau = [0,1,1,1,0,1,1,0,1]
la fonction(tableau, 0) doit renvoyer "0, 4, 7". n'hesitez pas a implementer la premiere fonction'''

def concat(phrase1, phrase2): #renvoie une phrase concatené a partir de 2 phrases
    phraseConcat = phrase1 + ", " + phrase2
    #renvoie la phrase concatené
    return phraseConcat 

def chaineOcuurences(tableau,occurence): #renvoie une chaine str avec toute les occurences choisie
    phrase = ""
    for k in range(len(tableau - 1)):
        if occurence == tableau[k]:
            concat(phrase,tableau[k])
    return phrase