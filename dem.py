import random

def baseMineur(): #importation du tableau
    list=[]
    for i in range(5):
    list.append([])
    for j in range(5):
        list[i].append("*")
    return list

def tableau(list):
    for i in list:
        print (i)


def mineHasard(mineBoum): #Répartition des mines
    totalMine=6
    while totalMine:
        x=random.radint(0,6)
        y=random.randint(0,6)
        if mineBoum[x][y]==0:
            mineBoum[x][y]==1

def selectionNb():
    x=int (input("Ligne"))
    y=int (input("Colonne"))

if selectionNb ==:
    print "Perdu!"
