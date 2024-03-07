import numpy as np
import random
from tkinter import *

player = True #Lorsque que le J1 joue player est à True, sinon False pour le J2
game_over = False
egalite = False
check = False
joueur1 = ""
joueur2 = ""
diagJouableIA = []
ligneJouableIA = []
colonneJouableIA = []
caseJouable = []
caseJouableIa = []

a = (3,3)
plateau = np.zeros(a, dtype=int)

###################### Jeu dans le terminal ######################
def start():
    """ Se lance au début du jeu pour demander le nombre de joueurs ainsi que leur noms """
    global joueur1, joueur2
    nbJoueur = int(input("Entrez nombre de joueurs :"))

    while(nbJoueur < 1 or nbJoueur > 2):
        nbJoueur = int(input("Veuillez saisir un nombre de joueurs valide (1/2) :"))

    if nbJoueur == 1:
        print("Veuillez choisir le niveau de l'IA :")
        print("1 : Niveau IA Facile")
        print("2 : Niveau IA Moyen")
        print("3 : Niveau IA Difficile")
        choixIA = int(input("Saisir votre choix :"))
        if choixIA == 1:
            print("Vous avez sélectionnez L'IA niveau Facile")
            joueur1 = input("Saisir votre nom :")
            print("Nom du joueur 1 :", joueur1)
            joueur2 = "IA"
            tourAvecIANoob()
        elif choixIA == 2:
            print("Vous avez sélectionnez L'IA niveau Moyen")
            joueur1 = input("Saisir votre nom :")
            print("Nom du joueur 1 :", joueur1)
            joueur2 = "IA"
            tourAvecIAMoyen()
        elif choixIA == 3:
            print("Vous avez sélectionnez l'IA niveau Difficile")
            joueur1 = input("Saisir votre nom :")
            print("Nom du joueur 1 :", joueur1)
            joueur2 = "IA"
            tourAvecIADifficile()
    elif nbJoueur == 2:
        joueur1 = input("Saisir nom du joueur 1 :")
        joueur2 = input("Saisir nom du joueur 2 :")
        print("Nom du joueur 1 :", joueur1)
        print("Nom du joueur 2 :", joueur2)
        tour()

def choixJoueur():
    """
    Permet de choisir le joueur de manière aléatoire qui jouera en premier
    Stocke le résultat dans une variable randomNumber
    Renvoie randomNumber
    """
    randomNumber = random.randint(1,2)
    global player
    if randomNumber == 1:
        player = True
        print("C'est le joueur 1 qui commence")
    if randomNumber == 2:
        player = False
        print("C'est le joueur 2 qui commence")
    return randomNumber

def verifPlacement(choixLigne,choixColonne):
    """
    Prend en paramètres le choix de la ligne et le choix de la colonne du joueur
    Permet de vérifier si l'emplacement choisi par le joueur est valide, si il ne joue pas en dehors du plateau
    Si c'est valide alors renvoie la ligne et la colonne choisi par le joueur
    """

    while(choixLigne >=3 or choixColonne >=3):
        choixLigne = int(input("Veuillez saisir une ligne valide :"))
        choixColonne = int(input("Veuillez saisir une colonne valide :"))
    return choixLigne,choixColonne

def verifPionPresent(ligne,col):
    """
    Prend en paramètres la ligne et la colonne choisi par le joueur
    Renvoie True si il y a un pion présent sur cette case, False sinon
    """

    if plateau[ligne,col] == 1 or plateau[ligne,col] == 2:
        return True
    return False
def finGame(plat):
    """
    Prend en paramètre le plateau du jeu
    Gère la fin de game donc vérifie si un joueur à gagné ou si il y a égalité
    Renvoie True si la partie est fini et False sinon
    """
    global egalite, joueur1, joueur2
    #Parcours de ligne
    for i in range(plat.shape[0]):
        if (plat[i,0] == plat[i,1] == plat[i,2]) and plat[i,0] != 0:
            if plat[i,0] == 1:
                print("Joueur 1 "+ joueur1 +" à gagné !")
                return True
            elif plat[i,0] == 2:
                print("Joueur 2 "+ joueur2 +" à gagné !")
                return True

    #Parcours de colonne
    for i in range(plat.shape[1]):
        if (plat[0,i] == plat[1,i] == plat[2,i]) and plat[0,i] != 0:
            if plat[0,i] == 1:
                print("Joueur 1 " + joueur1 +" à gagné !")
                return True
            elif plat[0,i] == 2:
                print("Joueur 2 " + joueur2 +" à gagné !")
                return True

    #Parcours de diagonale 1
    if (plat[0,0] == plat[1,1] == plat[2,2]) and plat[0,0] != 0:
        if plat[0, 0] == 1:
            print("Joueur 1 " + joueur1 + " à gagné !")
            return True
        elif plat[0, 0] == 2:
            print("Joueur 2 " + joueur2 + " à gagné !")
            return True

    #Parcours de diagonale 2
    if (plat[2, 0] == plat[1, 1] == plat[0, 2]) and plat[2,0] != 0:
        if plat[2, 0] == 1:
            print("Joueur 1 " + joueur1 + " à gagné !")
            return True
        elif plat[2, 0] == 2:
            print("Joueur 2 " + joueur2 + " à gagné !")
            return True

    #Egalité
    if not(0 in plat):
        egalite = True
        print("Egalité")
        return True

    return False

def tour():
    """
    Permet de gérer le système de tour par tour
    A chaque tour affiche le plateau à jour et demande au joueur de placer un pion, verifie si l'emplacement existe et si il est disponible
    Puis si c'est ok, place le pion à l'endroit choisi par le joueur
    """
    fin = False
    joueur = choixJoueur()
    if joueur == 1:
        print(plateau)
        choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
        choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))

        plateau[verifPlacement(choixLigne, choixColonne)] = 1
        print(plateau)

        while fin != True:
            print("Au tour du joueur 2")
            choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
            choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))
            while verifPionPresent(choixLigne,choixColonne) == True:
                print("Cette case est déjà prise, veuillez choisir une autre case :")
                print(plateau)
                choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
                choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))

            plateau[verifPlacement(choixLigne, choixColonne)] = 2
            print(plateau)
            if finGame(plateau) == True:
                fin = True
                break

            print("Au tour du joueur 1")
            choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
            choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))
            while verifPionPresent(choixLigne,choixColonne) == True:
                print("Cette case est déjà prise, veuillez choisir une autre case :")
                print(plateau)
                choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
                choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))

            plateau[verifPlacement(choixLigne, choixColonne)] = 1
            print(plateau)

            if finGame(plateau) == True:
                fin = True

        exit()

    elif joueur == 2:
        print(plateau)
        choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
        choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))

        plateau[verifPlacement(choixLigne, choixColonne)] = 2
        print(plateau)


        while fin != True:
            print("Au tour du joueur 1")
            choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
            choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))
            while verifPionPresent(choixLigne, choixColonne) == True:
                print("Cette case est déjà prise, veuillez choisir une autre case :")
                print(plateau)
                choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
                choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))

            plateau[verifPlacement(choixLigne, choixColonne)] = 1
            print(plateau)

            if finGame(plateau) == True:
                fin = True
                break

            print("Au tour du joueur 2")
            choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
            choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))
            while verifPionPresent(choixLigne, choixColonne) == True:
                print("Cette case est déjà prise, veuillez choisir une autre case :")
                print(plateau)
                choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
                choixColonne = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))

            plateau[verifPlacement(choixLigne, choixColonne)] = 2
            print(plateau)

            if finGame(plateau) == True:
                fin = True
        exit()


##################### IA NOOB ########################

def choixCaseRandom():
    """
    Choisi une ligne et une colonne aléatoirement dans le plateau pour le niveau de l'IA Facile
    Renvoie la ligne et la colonne choisi aléatoirement
    """
    randomLigne = random.randint(0,2)
    randomColonne = random.randint(0,2)
    return randomLigne, randomColonne

def verifCaseIADispo(ligne,col):
    """
    Prend en paramètres la ligne et la colonne de l'IA choisi et vérifie si cette case est déjà prise ou non
    Renvoie True si la case est disponible et Fals sinon
    """
    if plateau[ligne,col] == 1 or plateau[ligne,col] == 2:
        return False
    return True

def ChoixPlacementPionJ1():
    """
    Demande au J1 de chosir la ligne et la colonne où il aimerait jouer
    Renvoie la ligne et la colonne choisi par le J1
    """
    print(plateau)
    print("Tour de J1 :")
    choixLigne = int(input("Veuillez choisir la ligne où vous souhaitez jouer :"))
    choixCol = int(input("Veuillez choisir la colonne où vous souhaitez jouer :"))
    while verifPionPresent(choixLigne, choixCol) == True:
        print("Cette case est déjà prise, veuillez choisir une autre case :")
        print(plateau)
        choixLigne = int(input("Choisissez la ligne où vous souhaitez placer votre pion :"))
        choixCol = int(input("Choisissez la colonne où vous souhaitez placer votre pion :"))
    plateau[verifPlacement(choixLigne,choixCol)] = 1
    return choixLigne, choixCol

def iaNoob():
    """
    Joue aléatoirement
    Vérifie que la case choisi aléatoirement est dispo,
    si oui alors elle joue sinon elle choisi une autre case aléatoirement
    """
    print("Tour de L'IA :")
    IAligne, IAcolonne = choixCaseRandom()
    if verifCaseIADispo(IAligne,IAcolonne):
        plateau[IAligne,IAcolonne] = 2
    else:
        while verifCaseIADispo(IAligne,IAcolonne) == False:
            IAligne, IAcolonne = choixCaseRandom()
        plateau[IAligne,IAcolonne] = 2

##################### IA NOOB ########################

##################### IA MOYENNE ########################

def DoublonsColonneJouable(colonneIA):
    """
    Prend en paramètre la colonne choisi par l'IA et vérifie dans la liste  'ligneJouableIA' qui contient
    les coordonnées des lignes jouable par l'IA

    Vérifie que dans cette liste il n'y ai pas déjà la présence des coordonnées que l'on souhaite ajouter
    Si elles n'y sont pas alors on renvoie False
    Sinon on renvoie True
    """
    global ligneJouableIA
    for index in ligneJouableIA:
        if index == colonneIA:
            return True
    return False
def chercheCaseJouableIAColonne(lignej1):
    """
    Prend en paramètre la ligne joué par le Joueur 1
    Parcours la ligne joué par le Joueur 1

    Renvoie la ligne et la colonne jouable sur la ligne du Joueur 1
    """
    global colonneJouableIA
    colonneJouableIA = []
    for colonne in range(plateau.shape[1]):
        if plateau[lignej1,colonne] == 0:
            if DoublonsColonneJouable(colonne) == False:
                colonneJouableIA.append([lignej1,colonne])
    return colonneJouableIA

def DoublonsLigneJouable(ligneIA):
    """
    Prend en paramètre la ligne choisi par l'IA et vérifie dans la liste  'colonneJouableIA' qui contient
    les coordonnées des colonnes jouable par l'IA

    Vérifie que dans cette liste il n'y ai pas déjà la présence des coordonnées que l'on souhaite ajouter
    Si elles n'y sont pas alors on renvoie False
    Sinon on renvoie True
    """
    global ligneJouableIA
    for index in ligneJouableIA:
        if index == ligneIA:
            return True
    return False
def chercheCaseJouableIALigne(colonnej1):
    """
    Prend en paramètre la colonne joué par le Joueur 1
    Parcours la colonne joué par le Joueur 1

    Renvoie la ligne et la colonne jouable sur la colonne du Joueur 1
    """
    global ligneJouableIA
    ligneJouableIA = []
    for ligne in range(plateau.shape[0]):
        if plateau[ligne,colonnej1] == 0:
            if DoublonsLigneJouable(ligne) == False:
                ligneJouableIA.append([ligne,colonnej1])
    return ligneJouableIA

def DoublonsDiagJouable(ligneIA,colIA):
    """
    Prend en paramètre la ligne et la colonne choisi par l'IA et vérifie dans la liste  'diagJouableIA' qui contient
    les coordonnées des diagonales jouable par l'IA

    Vérifie que dans cette liste il n'y ai pas déjà la présence des coordonnées que l'on souhaite ajouter
    Si elles n'y sont pas alors on renvoie False
    Sinon on renvoie True
    """
    global diagJouableIA
    for index,coordonnee in enumerate (diagJouableIA):
        if coordonnee == [ligneIA, colIA]:
            return True
    return False

def chercheCaseJouableIADiag(lignej1,colj1):
    """
    Prend en paramètres la ligne et la colonne joué du Joueur 1
    En fonction de où joue le Joueur 1, on vérifie la diagonale 1 ou la diagonale 2 ou les 2
    On stock ensuite les coordonnées jouable sur les diagonales dans la liste 'diagJouableIA'

    Renvoie les coordonnées des cases jouables
    """
    global diagJouableIA
    diagJouableIA = []
    # Si le J1 place son pion en [0,0] ou [2,2]
    if (lignej1 == 0 and colj1 == 0) or (lignej1 == 2 and colj1 == 2):
        if plateau[0,0] == 1 or plateau[2,2] == 1:
            # Parcours de la diag 1
            for i in range(plateau.shape[0]):
                if plateau[i,i] == 0:
                    if DoublonsDiagJouable(i,i) == False:
                        diagJouableIA.append([i,i])

    # Si le J1 place son pion en [2,0] ou [0,2]
    if (lignej1 == 2 and colj1 == 0) or (lignej1 == 0 and colj1 == 2):
        if plateau[2,0] == 1 or plateau[0,2] == 1:
            # Parcours de la diag 2
                if plateau[2,0] == 0:
                    if DoublonsDiagJouable(2,0) == False:
                        diagJouableIA.append([2,0])

                if plateau[1,1] == 0:
                    if DoublonsDiagJouable(1,1) == False:
                        diagJouableIA.append([1,1])
                if plateau[0,2] == 0:
                    if DoublonsDiagJouable(0,2) == False:
                        diagJouableIA.append([0,2])

    # Si le J1 place son pion en [1,1]
    if (lignej1 == 1 and colj1 == 1):
        if plateau[1,1] == 1:
            # Parcours de la diag 1
            for i in range(plateau.shape[0]):
                if plateau[i,i] == 0:
                    if DoublonsDiagJouable(i,i) == False:
                        diagJouableIA.append([i,i])

            # Parcours de la diag 2
            if plateau[2, 0] == 0:
                if DoublonsDiagJouable(2,0) == False:
                    diagJouableIA.append([2, 0])

            if plateau[1, 1] == 0:
                if DoublonsDiagJouable(1,1) == False:
                    diagJouableIA.append([1, 1])

            if plateau[0, 2] == 0:
                if DoublonsDiagJouable(0,2) == False:

                    diagJouableIA.append([0, 2])

    return diagJouableIA

def caseJouableIA(ligne,col):
    """
    Prend en paramètres la ligne et la colonne joué du Joueur 1
    Stock toutes les cases jouables dans une liste 'caseJouable'

    Si les liste 'ligneJouable', 'colonneJouable' et 'diagJouable' sont vides
    alors on prend des coorodnnées aléatoires et on regarde si elles sont dispo,
    Si oui alors on les stock dans 'caseJouable' sinon on re fais un random

    Renvoie les toutes les cases jouables par l'IA
    """
    global caseJouable
    caseJouable = []
    ligneJouable = []
    colonneJouable = []
    diagJouable = []
    ligneJouable = chercheCaseJouableIALigne(ligne)
    colonneJouable = chercheCaseJouableIAColonne(col)
    diagJouable = chercheCaseJouableIADiag(ligne,col)

    if ligneJouable == [] and colonneJouable == [] and diagJouable == []:
        IAligne, IAcolonne = choixCaseRandom()
        if verifCaseIADispo(IAligne, IAcolonne):
            caseJouable = [IAligne, IAcolonne]
        else:
            while verifCaseIADispo(IAligne, IAcolonne) == False:
                IAligne, IAcolonne = choixCaseRandom()
            caseJouable = [IAligne, IAcolonne]
    else:
        caseJouable = ligneJouable + colonneJouable + diagJouable
    return caseJouable

def verifPresentj2Ligne(colj1):
    """
    Prend en paramètre la colonne joué du Joueur 1
    Parcours chaque ligne de la colonne
    Vérifie si sur cette colonne il y a la présence du Joueur 2

    Renvoie True si oui et False sinon
    """
    j2Present = False
    for elt in range(plateau.shape[0]):
        if plateau[elt,colj1] == 2:
            j2Present = True
            return j2Present,
    return j2Present

def verifPresentj2Col(lignej1):
    """
    Prend en paramètre la ligne joué du Joueur 1
    Parcours chaque colonne de cette ligne
    Vérifie si sur cette ligne il y a la présence du Joueur 2

    Renvoie True si oui et False sinon
    """
    j2Present = False
    for element in range(plateau.shape[1]):
        if plateau[lignej1,element] == 2:
            j2Present = True
            return j2Present
    return j2Present

def verifPresentj2Diag1(lignej1,colj1):
    """
    Prend en paramètre la ligne et la colonne joué du Joueur 1
    Vérifie si sur diagonnale1 il y a la présence du Joueur 2

    Renvoie True si oui et False sinon
    """
    j2Present = False
    # Si le J1 place son pion en [0,0] ou [2,2]
    if (lignej1 == 0 and colj1 == 0) or (lignej1 == 2 and colj1 == 2) or (lignej1 == 1 and colj1 == 1):
        # Parcours de la diag 1
        for i in range(plateau.shape[0]):
            if plateau[i, i] == 2:
                j2Present = True
                return j2Present
    return j2Present


def verifPresentj2Diag2(lignej1, colj1):
    """
    Prend en paramètre la ligne et la colonne joué du Joueur 1
    Vérifie si sur la diagonnale2 il y a la présence du Joueur 2

    Renvoie True si oui et False sinon
    """
    j2Present = False
    # Si le J1 place son pion en [0,0] ou [2,2]
    if (lignej1 == 2 and colj1 == 0) or (lignej1 == 1 and colj1 == 1) or (lignej1 == 0 and colj1 == 2):
        # Parcours de la diag 2
        if plateau[2, 0] == 2:
            j2Present = True
            return j2Present

        if plateau[1, 1] == 2:
            j2Present = True
            return j2Present

        if plateau[0, 2] == 2:
            j2Present = True
            return j2Present
    return j2Present

def j1blockable(lignej1,colj1):
    """
    Prend en paramètres la ligne et la colonne joué du Joueur 1
    Parcours la ligne puis la colonne puis les diagonnales si possible
    Vérifie si il y 2 fois le Joueur 1

    Si oui , renvoie True ( avec la précision de si c'est sur la ligne ou la colonne ou la diag ) et False sinon
    """
    global check
    compteurNombrej1 = 0
    blockable = False
    ligne = False
    col = False
    diag1 = False
    diag2 = False
    verif = False

    # Parcours de ligne du j1
    for colonne in range(plateau.shape[1]):
        if plateau[lignej1,colonne] == 1 and verifPresentj2Col(lignej1) == False:
            compteurNombrej1 += 1
            if compteurNombrej1 == 2:
                blockable = True
                ligne = True
                return blockable, ligne, col, diag1, diag2, verif
    compteurNombrej1 = 0

    # Parcours de la colonne du j1
    for ligneCheck in range(plateau.shape[0]):
        if plateau[ligneCheck,colj1] == 1 and verifPresentj2Ligne(colj1) == False:
            compteurNombrej1 += 1

            if compteurNombrej1 == 2:
                blockable = True
                col = True
                return blockable, ligne, col, diag1, diag2, verif
    compteurNombrej1 = 0

    # Parcours de la diag 1
    if (lignej1 == 0 and colj1 == 0) or (lignej1 == 1 and colj1 == 1) or (lignej1 == 2 and colj1 == 2):
        for i in range(plateau.shape[0]):
            if plateau[i, i] == 1 and verifPresentj2Diag1(lignej1,colj1) == False:
                compteurNombrej1 += 1

                if compteurNombrej1 == 2:
                    blockable = True
                    diag1 = True
                    return blockable, ligne, col, diag1, diag2, verif
        compteurNombrej1 = 0

    # Parcours de la diag 2
    if (lignej1 == 2 and colj1 == 0) or (lignej1 == 1 and colj1 == 1) or (lignej1 == 0 and colj1 == 2):
        if plateau[2, 0] == 1 and verifPresentj2Diag2(lignej1,colj1) == False:
            compteurNombrej1 += 1
        else:
            compteurNombrej1 = 0

        if plateau[1, 1] == 1 and verifPresentj2Diag2(lignej1,colj1) == False:
            compteurNombrej1 += 1

            if compteurNombrej1 == 2:
                blockable = True
                diag2 = True
                verif = True
                return blockable, ligne, col, diag1, diag2, verif
        else:
            compteurNombrej1 = 0

        if plateau[0, 2] == 1 and verifPresentj2Diag2(lignej1,colj1) == False:
            compteurNombrej1 += 1

            if compteurNombrej1 == 2:
                blockable = True
                diag2 = True
                return blockable, ligne, col, diag1, diag2, verif
        else:
            compteurNombrej1 = 0
    return blockable, ligne, col, diag1, diag2, verif

def blockj1(lignej1,colj1,blockable,ligne,col,diag1,diag2,verif):
    """
    Prend en paramètres lignej1,colj1,blockable,ligne,col,diag1,diag2,verif
    'blockable,ligne,col,diag1,diag2,verif' sont les booléens que renvoient la fonction 'j1blockable'
    En fonction de si la case est vide et si il faut bloquer sur la ligne ou la colonne ou la diag du pion joué par le J1,

    Renvoie les coordoonées de la case que l'IA doit bloquer
    """
    compteurNombrej1 = 0
    colonneia = 0
    ligneia = 0

    # Parcours de ligne du j1
    if blockable == True and ligne == True:
        for colonne in range(plateau.shape[1]):
            if plateau[lignej1,colonne] == 0:
                colonneia = colonne
                ligneia = lignej1
                return ligneia,colonneia

    # Parcours de la colonne du j1
    if blockable == True and col == True:
        for ligne in range(plateau.shape[0]):
            if plateau[ligne,colj1] == 0:
                colonneia = colj1
                ligneia = ligne
                return ligneia,colonneia

    # Parcours de la diag 1
    if blockable == True and diag1 == True:
        for j in range(plateau.shape[0]):
            if plateau[j, j] == 0:
                colonneia = j
                ligneia = j
                return ligneia, colonneia

    # Parcours de la diag 2
    if blockable == True and diag2 == True:
        if verif:
            ligneia = 0
            colonneia = 2
            return ligneia, colonneia
        else:
            ligneia = 1
            colonneia = 1
            return ligneia, colonneia


def iaMoyen(ligneJ1,colJ1):
    """
    Prend en paramètres la ligne et la colonne joué par le Joueur 1
    Permet de faire jouer l'IA
    Si le J1 peut être bloqué alors l'IA le bloque
    Sinon elle joue aléatoirement
    """
    global caseJouableIa
    print("Tour de L'IA :")
    blockable, ligne,col,diag1,diag2,verif = j1blockable(ligneJ1, colJ1)
    if blockable:
        ligneIABlock, colIABlock = blockj1(ligneJ1, colJ1, blockable,ligne,col,diag1,diag2,verif)
        plateau[ligneIABlock, colIABlock] = 2
    else:
        caseJouableIa = caseJouableIA(ligneJ1, colJ1)
        randomCoordonnee = random.randint(0,len(caseJouableIa)-1)
        coordonne = caseJouableIa[randomCoordonnee]
        if verifCaseIADispo(coordonne[0],coordonne[1]):
            plateau[coordonne[0], coordonne[1]] = 2
        else:
            while verifCaseIADispo(coordonne[0], coordonne[1]) == False:
                randomCoordonnee = random.randint(0, len(caseJouableIa) - 1)
                coordonne = caseJouableIa[randomCoordonnee]

##################### IA MOYENNE ########################

##################### IA DIFFICILE ########################

def cherchej2():
    """
    Parcours le plateau et cherche si il y a la présence du Joueur 2 ( L'IA )
    Si oui, renvoie True et les coordonnées de la case où se trouve le J2 ( L'IA )
    Sinon, renvoie False
    """
    for ligne in range(plateau.shape[0]):
        for col in range(plateau.shape[1]):
            if plateau[ligne,col] == 2:
                return True,ligne,col
    return False,None,None

def verifPresentj1Col(lignej2):
    """
    Prend en paramètre la ligne joué du Joueur 2 ( L'IA )
    Parcours chaque colonne de cette ligne
    Vérifie si sur cette ligne il y a la présence du Joueur 1

    Renvoie True si oui et False sinon
    """
    j1Present = False
    for elt in range(plateau.shape[0]):
        if plateau[lignej2,elt] == 1:
            j1Present = True
            return j1Present
    return j1Present

def verifPresentj1Ligne(colj2):
    """
    Prend en paramètre la colonne joué du Joueur 2 ( L'IA )
    Parcours chaque ligne de cette colonne
    Vérifie si sur cette colonne il y a la présence du Joueur 1

    Renvoie True si oui et False sinon
    """
    j1Present = False
    for element in range(plateau.shape[1]):
        if plateau[element,colj2] == 1:
            j1Present = True
            return j1Present
    return j1Present

def verifPresentj1Diag1(lignej2,colj2):
    """
    Prend en paramètre la ligne et la colonne joué du Joueur 2 ( L'IA )
    Vérifie si sur diagonnale1 il y a la présence du Joueur 1

    Renvoie True si oui et False sinon
    """
    j1Present = False
    # Si le J1 place son pion en [0,0] ou [2,2]
    if (lignej2 == 0 and colj2 == 0) or (lignej2 == 2 and colj2 == 2) or (lignej2 == 1 and colj2 == 1):
        # Parcours de la diag 1
        for i in range(plateau.shape[0]):
            if plateau[i, i] == 1:
                j1Present = True
                return j1Present
    return j1Present

def verifPresentj1Diag2(lignej2,colj2):
    """
    Prend en paramètre la ligne et la colonne joué du Joueur 2 ( L'IA )
    Vérifie si sur diagonnale2 il y a la présence du Joueur 1

    Renvoie True si oui et False sinon
    """
    j1Present = False
    # Si le J1 place son pion en [0,0] ou [2,2]
    if (lignej2 == 2 and colj2 == 0) or (lignej2 == 1 and colj2 == 1) or (lignej2 == 0 and colj2 == 2):
        # Parcours de la diag 2
        if plateau[2, 0] == 1:
            j1Present = True
            return j1Present

        if plateau[1, 1] == 1:
            j1Present = True
            return j1Present

        if plateau[0, 2] == 1:
            j1Present = True
            return j1Present
    return j1Present
def gainj2(lignej2,colj2):
    """
    Prend en paramètre la ligne et la colonne joué du Joueur 2 ( L'IA )
    Parcours la ligne, la colonne, les diagonnales si possibles du pion joué par le Joueur 2
    Vérifie si il y a 2 fois le pion du J2 sur cette même ligne ou colonne ou diag

    Si oui renvoie True avec la précision si c'est sur la ligne, la colonne ou la diag du pion joué du J2
    Sinon renvoie False
    """
    compteurCaseJ2Ligne = 0
    compteurCaseJ2Col = 0
    compteurCaseJ2Diag1 = 0
    compteurCaseJ2Diag2 = 0
    gagnable = False
    ligne = False
    col = False
    diag1 = False
    diag2 = False
    verif = False

    # Parcours de ligne du j2
    for colonne in range(plateau.shape[1]):
        if plateau[lignej2, colonne] == 2 and verifPresentj1Col(lignej2) == False:
            compteurCaseJ2Ligne += 1
            if compteurCaseJ2Ligne == 2 :
                gagnable = True
                ligne = True
                return gagnable, ligne, col, diag1, diag2, verif

    # Parcours de la colonne du j2
    for ligne in range(plateau.shape[0]):
        if plateau[ligne, colj2] == 2 and verifPresentj2Ligne(colj2) == False:
            compteurCaseJ2Col += 1
            if compteurCaseJ2Col == 2:
                gagnable = True
                col = True
                return gagnable, ligne, col, diag1, diag2, verif

    # Parcours de la diag 1
    if (lignej2 == 0 and colj2 == 0 or lignej2 == 1 and colj2 == 1 or lignej2 == 2 and colj2 == 2):
        for i in range(plateau.shape[0]):
            if plateau[i, i] == 2 and verifPresentj1Diag1(lignej2,colj2) == False:
                compteurCaseJ2Diag1 += 1
                if compteurCaseJ2Diag1 == 2:
                    gagnable = True
                    diag1 = True
                    return gagnable, ligne, col, diag1, diag2, verif

    # Parcours de la diag 2
    if (lignej2 == 2 and colj2 == 0 or lignej2 == 1 and colj2 == 1 or lignej2 == 0 and colj2 == 2):
        if plateau[2, 0] == 2 and verifPresentj1Diag2(lignej2,colj2) == False:
            compteurCaseJ2Diag2 += 1

        if plateau[1, 1] == 2 and verifPresentj1Diag2(lignej2,colj2) == False:
            compteurCaseJ2Diag2 += 1
            if compteurCaseJ2Diag2 == 2:
                gagnable = True
                diag2 = True
                verif = True
                return gagnable, ligne, col, diag1, diag2, verif

        if plateau[0, 2] == 2 and verifPresentj1Diag2(lignej2,colj2) == False:
            compteurCaseJ2Diag2 += 1
            if compteurCaseJ2Diag2 == 2:
                gagnable = True
                diag2 = True
                return gagnable, ligne, col, diag1, diag2, verif
    return gagnable, ligne, col, diag1, diag2, verif

def caseVide(lignej2,colj2,gagnable,ligne,col,diag1,diag2,verif):
    """
    Prend en paramètres la ligne et la colonne joué par le Joueur 2 ( l'IA )
    'gagnable,ligne,col,diag1,diag2,verif' sont les booléens renvoyés par la fonction gainj2
    Si il y a un gain de l'IA, alors on parcours soit la ligne soit la colonne soit la diag en fonction de où se situe le gain de l'IA
    On vérifie qu'il est possible de poser un pion

    Si oui, on renvoie les coordonnées de la case où il y a gain de l'IA
    Sinon, on renvoie rien
    """
    compteurNombrej1 = 0
    colonneia = 0
    ligneia = 0

    # Parcours de ligne du j1
    if gagnable == True and ligne == True:
        for colonne in range(plateau.shape[1]):
            if plateau[lignej2,colonne] == 0:
                colonneia = colonne
                ligneia = lignej2
                return ligneia,colonneia

    # Parcours de la colonne du j1
    if gagnable == True and col == True:
        for ligne in range(plateau.shape[0]):
            if plateau[ligne,colj2] == 0:
                colonneia = colj2
                ligneia = ligne
                return ligneia,colonneia

    # Parcours de la diag 1
    if gagnable and diag1:
        for j in range(plateau.shape[0]):
            if plateau[j, j] == 0:
                colonneia = j
                ligneia = j
                return ligneia, colonneia

    # Parcours de la diag 2
    if gagnable and diag2:
        if verif:
            ligneia = 1
            colonneia = 1
            return ligneia, colonneia
        else:
            ligneia = 2
            colonneia = 0
            return ligneia, colonneia



def iaDifficile(ligneJ1, colJ1):
    """
    Prend en paramètres la ligne et la colonne joué par le Joueur 1
    Permet de faire joué l'IA difficile
    Lorsque l'IA peut bloquer elle bloque, si elle peut gagner elle gagne, si elle ne peut ni bloquer ni gagner, elle joue aléatoirement
    """
    global caseJouableIa
    print("Tour de L'IA :")
    present, lignej2, colj2 = cherchej2()
    blockable, lignej1, colj1, diag1, diag2, verif = j1blockable(ligneJ1, colJ1)

    if blockable and present:
        gagnable, ligneJ2, colJ2, Diag1, Diag2, verif2 = gainj2(lignej2, colj2)
        if gagnable:
            ligneIAGain, colIAGain = caseVide(lignej2, colj2, gagnable, ligneJ2, colJ2, Diag1, Diag2, verif2)
            plateau[ligneIAGain, colIAGain] = 2
        else:
            ligneIABlock, colIABlock = blockj1(ligneJ1, colJ1, blockable, lignej1, colj1, diag1, diag2, verif)
            plateau[ligneIABlock, colIABlock] = 2

    elif blockable:
        ligneIABlock, colIABlock = blockj1(ligneJ1, colJ1, blockable, lignej1, colj1, diag1, diag2, verif)
        plateau[ligneIABlock, colIABlock] = 2
    else:
        caseJouableIa = caseJouableIA(ligneJ1, colJ1)
        randomCoordonnee = random.randint(0, len(caseJouableIa) - 1)
        coordonne = caseJouableIa[randomCoordonnee]
        if verifCaseIADispo(coordonne[0], coordonne[1]):
            plateau[coordonne[0], coordonne[1]] = 2
        else:
            while verifCaseIADispo(coordonne[0], coordonne[1]) == False:
                randomCoordonnee = random.randint(0, len(caseJouableIa) - 1)
                coordonne = caseJouableIa[randomCoordonnee]

##################### IA DIFFICILE ########################

##################### TOUR PAR TOUR ########################


def tourAvecIADifficile():
    """
    Permet de gérer la gestion de tour par tour avec l'IA difficile
    """
    global plateau
    fin = finGame(plateau)
    while fin != True:
        lignej1, colj1 = ChoixPlacementPionJ1()
        if finGame(plateau):
            print(plateau)
            exit()
        iaDifficile(lignej1,colj1)
        if finGame(plateau):
            print(plateau)
            exit()


def tourAvecIAMoyen():
    """
    Permet de gérer la gestion de tour par tour avec l'IA moyenne
    """
    global plateau
    fin = finGame(plateau)
    while fin != True:
        lignej1, colj1 = ChoixPlacementPionJ1()
        if finGame(plateau):
            print(plateau)
            exit()
        iaMoyen(lignej1,colj1)
        if finGame(plateau):
            print(plateau)
            exit()
def tourAvecIANoob():
    """
    Permet de gérer la gestion de tour par tour avec l'IA Noob
    """
    global plateau
    fin = finGame(plateau)
    while fin != True:
        ChoixPlacementPionJ1()
        if finGame(plateau):
            print(plateau)
            exit()
        iaNoob()
        if finGame(plateau):
            print(plateau)
            exit()


##################### TOUR PAR TOUR ########################

start()

################### Jeu dans le terminal #######################





