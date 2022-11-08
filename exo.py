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
        #retourner un message d'erreur car on ne divise pas par 0
        return "error"

def modulo(x,y):
    if x != 0 :
        return x % y
    else:
        return "error"

def CalculSalaireParSeconde(SalaireHoraire, HeureParJourOuvrable,nb_JourOuvrable):
    #Assigner a salaire annuel, le salaire par nombre d'heure travaillé par an
    salaireAnnuel =  SalaireHoraire * HeureParJourOuvrable * nb_JourOuvrable
    #Calculer, puis assigner a nombreParSecondeParAn , le nombre de seconde dans une année non bisextile
    nombreDeSecondeParAn = 60 * 60 * 24 *365
    #retourner le salaire Annuel divisé par le nombre de seconde par An
    return salaireAnnuel / nombreDeSecondeParAn

def CalculSalaireNet(SalaireBrut, coeff):
    #Calculer puis Assigner a taxe, le montant des taxes a retirer
    taxe = SalaireBrut * (coeff / 100)
    #retourner le salaire net final
    return salaireNet - taxe


def CalculSalaire(SalaireBrut, public):
    #si j'occupe un poste de la fonction publique
    if public:
        #alors je retourne le salaire brut -15% de taxe
        return CalculSalaireNet(SalaireBrut, 15)
    #sinon, c'est que je travaille dans le secteur privé
    else:
        #alors je retourne le salaire brut -23% de taxes
        return CalculSalaireNet(SalaireBrut, 23)