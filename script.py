from math import dist
import random

distanteOrase = [
#   CT  BV   SB   BUC
    [0, 400, 500, 300],#CT
    [400, 0, 300, 500],#BV
    [500, 300, 0, 400],#SB
    [300, 500, 400, 0]#BUC
]

#Trebuie sa inceapa cu o solutie initiala. Aceasta este functia care o construieste:

def construiescSolutieAleatorie(distanteOrase):
    orase= list(range(len(distanteOrase))) #declar o lista de orase ce va fi ca cea primita ca parametru
    configuratieNouaDeOrase=[] #declar o lista ce va tine noua configuratie de orase

    for i in range(len(distanteOrase)): # se trece prin fiecare oras  
        orasRandom = orase[random.randint(0,len(orase)-1)] #iau un oras random din lista de orase 
        configuratieNouaDeOrase.append(orasRandom) # il adaug in noua configuratie
        orase.remove(orasRandom) # il sterg din lista tuturor oraselor pentru a nu il putea alege din nou
    
    return configuratieNouaDeOrase

# Trebuie sa creez o functie care calculeaza distanta pentru o anumita configuratie:

def calculezDistantaUneiConfiguratii(distantelePredefinite,configuratie):
    distanta = 0
    for i in range(len(configuratie)):
        distanta+= distantelePredefinite[configuratie[i-1]][configuratie[i]] #unde config(i-1) e previous city si config(i) e cel curent 300+ 2130: 500+300+500+300=1600
    return distanta


#Trebuie sa fac o functie care pe baza unei configuratii intoarce fiecare vecin a acestuia, un vecin difera printr-o interschimbare.
def construiesteVecini(configuratie):
    vecini=[]
    for i in range(len(configuratie)):
        for j in range(i+1,len(configuratie)):
            vecin=configuratie.copy()
            vecin[i]=configuratie[j]
            vecin[j]=configuratie[i]
            vecini.append(vecin)
    return vecini


# Fac o funtie pt a stabili cel mai bun vecin adica cu cea mai mica ruta in km

def celMaiBunVecin(distantelePredefinite,vecini):
    ceaMaiBunaDistanta=calculezDistantaUneiConfiguratii(distantelePredefinite,vecini[0]) #plec prin a stabilii cea mai scurta ruta prima ruta din vecini
    celMaiBunVecin=vecini[0]#stabilesc cel mai bun vecin drept primul

    for vecin in vecini: #pt fiecare vecin
        distantaCurenta=calculezDistantaUneiConfiguratii(distantelePredefinite,vecin) #calculez distanta vecinului
        if distantaCurenta<ceaMaiBunaDistanta: #daca este mai scurta decat cea mai buna de pana acm updatez
            ceaMaiBunaDistanta=distantaCurenta
            celMaiBunVecin=vecin
      
    return celMaiBunVecin,ceaMaiBunaDistanta


#Algoritmul in sine

def HillClimbing(distantePredefinite):
    configuratiaCurenta=construiescSolutieAleatorie(distantePredefinite)
    distantaCurenta=calculezDistantaUneiConfiguratii(distantePredefinite,configuratiaCurenta)
    vecini = construiesteVecini(configuratiaCurenta)
    celMaiBunVecinGasit,distantaCeluiMaiBunVecin=celMaiBunVecin(distantePredefinite,vecini)

    while distantaCeluiMaiBunVecin<distantaCurenta: #cat timp diostanta celui mai bun vecin este mai scurta decat distanta curenta adica pana nu segaseste vreo distanta mai scurta
        configuratiaCurenta=celMaiBunVecinGasit
        distantaCurenta=distantaCeluiMaiBunVecin
        vecini=construiesteVecini(configuratiaCurenta)
        celMaiBunVecinGasit,distantaCeluiMaiBunVecin=celMaiBunVecin(distantePredefinite,vecini)

    return configuratiaCurenta,distantaCurenta

print(HillClimbing(distanteOrase))
