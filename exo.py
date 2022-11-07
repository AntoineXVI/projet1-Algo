DEBUT

print("hello world")

r = 12000
s = 1250
e = 10
rh = 230

assertionUn = (( (365 * 3) / (24 - (16 - 8)) ) * (rh) > r ) == (e * s < r ) 

assertionUnPtUn = (( (365 * 3) / (24 - (16 - 8)) ) * (rh) > r ) -> V
1095 / 16 = 68,4375 / 
68,4375 * 230 = 15 740,625/ 
15 740,625 > 12000

assertionUnPtDeux = (e * s < r ) -> F
10 * 1250 = 12500/ 
12500 < 12000

(( (365 * 3) / (24 - (16 - 8)) ) * (rh) > r ) == (e * s < r ) -> F
#assertionUn = assertionUnPtUn == assertionUnPtDeux = False

assertionDeux = ((365 * 3) / (4 - (12 - 8)) * (rh) > r ) == (e * s < r ) 

assertionDeuxPtUn = ((365 * 3) / (4 - (12 - 8)) * (rh) > r ) -> F
1095 / 0 #impossible de diviser par 0


assertionDeuxPtDeux = (e * s < r ) -> F
10 * 1250 = 12500/ 
12500 < 12000

((365 * 3) / (4 - (12 - 8)) * (rh) > r ) == (e * s < r ) -> V
#assertionUn = assertionUnPtUn == assertionUnPtDeux = True

def retournerSixPlusTrois():
    return 6 + 3

def retournerSixPlusX(x):
    return 6 + x
    

print("qui vole un " + retournerSixPlusTrois() + "vole un boeuf ")

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulo(x,y):
    return x % y

def CalculSalaireParSeconde(SalaireHoraire, HeureParJourOuvrable,nb_JourOuvrable):
    salaireParSeconde =  ((SalaireHoraire * HeureParJourOuvrable) * nb_JourOuvrable) / 3600
    return salaireParSeconde

def CalculSalaireNet(SalaireBrut, coeff):
    salaireNet = (SalaireBrut * coeff) / 100
    return SalaireNet


FIN


