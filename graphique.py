from tkinter import *
import numpy as np

################### Jeu partie graphique ##############################

a = (3,3)
plateau = np.zeros(a, dtype=int)

player = True #Lorsque que le J1 joue player est à True, sinon False pour le J2
game_over = False
egalite = False
root = Tk()
boutons = []
tour_joueur = StringVar()
tour_joueur.set("Tour du Joueur 1")

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
    global egalite
    gagnant = ""
    #Parcours de ligne
    for i in range(plat.shape[0]):
        if (plat[i,0] == plat[i,1] == plat[i,2]) and plat[i,0] != 0:
            print("Joueur "+ str(plat[i,0]) +" à gagné !")
            return True

    #Parcours de colonne
    for i in range(plat.shape[1]):
        if (plat[0,i] == plat[1,i] == plat[2,i]) and plat[0,i] != 0:
            print("Joueur " + str(plat[0,i]) +" à gagné !!")
            return True

    #Parcours de diagonale 1
    if (plat[0,0] == plat[1,1] == plat[2,2]) and plat[0,0] != 0:
        print("Joueur " + str(plat[0, 0]) +" à gagné !!!")
        return True

    #Parcours de diagonale 2
    if (plat[2, 0] == plat[1, 1] == plat[0, 2]) and plat[2,0] != 0:
        print("Joueur " + str(plat[2, 0]) + " à gagné !!!!")
        return True

    #Egalité
    if not(0 in plat):
        egalite = True
        gagnant = "égalité"
        print("Egalité")
        return True

    return False


def clicked(idx):
    """
    Prend en paramètre idx qui est l'indice du bouton qui se trouve dans la liste 'boutons'
    Vérifie si la partie est fini, si elle n'est pas fini, alors recupère les coordonnées du bouton choisi par
    le joueur et écris 'X' si c'est joueur 1 et 'O' si joueur 2
    Elle écrit aussi l'état de la partie avec le joueur gagnant ou égalité en-dessous du plateau
    """
    global player, game_over, egalite
    if not game_over:
        coordonne = boutons[idx].grid_info()
        ligne = coordonne["row"]
        col = coordonne["column"]

        if not verifPionPresent(ligne,col):
            if player:
                afficheTourJoueur()
                boutons[idx].config(text="X")
                plateau[ligne, col] = 1
                changeJoueur()
            else:
                afficheTourJoueur()
                boutons[idx].config(text="O")
                plateau[ligne, col] = 2
                changeJoueur()

            if finGame(plateau):
                game_over = True
                if egalite:
                    tour_joueur.set("Egalité !")
                elif not player:
                    tour_joueur.set("Joueur 1 à gagné !")
                    colorButtons(plateau)
                else:
                    tour_joueur.set("Joueur 2 à gagné !")
                    colorButtons(plateau)

def changeJoueur():
    """
    Permet de gérer le système de tour par tour qui récupère la variable player qui est un bool qui permet de définir quel joueur doit jouer
    Ensuite à chaque fois alterner entre True et False ( J1 = True et J2 = False )
    """
    global player
    player = not player
    afficheTourJoueur()

def afficheTourJoueur():
    """ Prend en compte quel joueur doit jouer et ensuite affiche le nom du joueur suivant qui doit jouer """
    global player
    if player:
        tour_joueur.set("Tour du Joueur 1 (X)")
    else:
        tour_joueur.set("Tour du Joueur 2 (O)")

def buttons():
    """ Crée les 9 boutons du plateau """
    for i in range(9):
        bouton = Button(root, font=("Arial", 24), width=5, height=2, command= lambda index=i: clicked(index))
        bouton.grid(row = i//3, column = i%3)
        boutons.append(bouton)

def colorButtons(plat):
    """
    Prend en paramètre le plateau du jeu
    Permet de colorier les boutons du joueur gagnant en vert
    """
    # Parcours de ligne
    for i in range(plat.shape[0]):
        if (plat[i, 0] == plat[i, 1] == plat[i, 2]) and plat[i, 0] != 0:
            for j in range(3):
                idx = i*3+j
                boutons[idx].config(bg="green")

    # Parcours de colonne
    for i in range(plat.shape[1]):
        if (plat[0, i] == plat[1, i] == plat[2, i]) and plat[0, i] != 0:
            for j in range(3):
                idx = j * 3 + i
                boutons[idx].config(bg="green")

    # Parcours de diagonale 1
    if (plat[0, 0] == plat[1, 1] == plat[2, 2]) and plat[0, 0] != 0:
        for j in range(3):
            idx = j * 3 + j
            boutons[idx].config(bg="green")

    # Parcours de diagonale 2
    if (plat[2, 0] == plat[1, 1] == plat[0, 2]) and plat[2, 0] != 0:
        for j in range(3):
            idx = j * 3 + (2-j)
            boutons[idx].config(bg="green")

def decolorButtons(plat):
    """
    Prend en paramètre le plateau du jeu
    Décolore tous les boutons du plateau, pour remettre la couleur originale
    """
    # Parcours de ligne
    for i in range(plat.shape[0]):
        if (plat[i, 0] == plat[i, 1] == plat[i, 2]) and plat[i, 0] != 0:
            for j in range(3):
                idx = i * 3 + j
                boutons[idx].config(bg="SystemButtonFace")

    # Parcours de colonne
    for i in range(plat.shape[1]):
        if (plat[0, i] == plat[1, i] == plat[2, i]) and plat[0, i] != 0:
            for j in range(3):
                idx = j * 3 + i
                boutons[idx].config(bg="SystemButtonFace")

    # Parcours de diagonale 1
    if (plat[0, 0] == plat[1, 1] == plat[2, 2]) and plat[0, 0] != 0:
        for j in range(3):
            idx = j * 3 + j
            boutons[idx].config(bg="SystemButtonFace")

    # Parcours de diagonale 2
    if (plat[2, 0] == plat[1, 1] == plat[0, 2]) and plat[2, 0] != 0:
        for j in range(3):
            idx = j * 3 + (2 - j)
            boutons[idx].config(bg="SystemButtonFace")
def reset():
    """
    Lorsque le bouton reset est crée,
    Parcours tous le plateau et décolore tous les boutons du jeu et met game_over à False
    """
    global plateau, game_over
    for ligne in range(plateau.shape[0]):
        for col in range(plateau.shape[1]):
            decolorButtons(plateau)
            plateau[ligne,col] = 0
    for i in range(9):
        boutons[i].config(text="")
    tour_joueur.set("")
    afficheTourJoueur()
    game_over = False

def game():
    """ Fonction qui permet de lancer le jeu"""

    afficheTourJoueur()
    buttons()

# Création d'une fenêtre fils avec frame pour afficher le tour du joueur
frameTexteTour = Frame(root)
frameTexteTour.place(x=50,y=300, width=300, height=300)
label = Label(frameTexteTour, textvariable=tour_joueur, font=("Arial", 16))
label.place(x=10, y=10, width=200,height=30)

#titre au dessus boutons
frameTitre = Frame(root)
frameTitre.place(x=350,y=0,width=300,height=50)
titre = Label(frameTitre, text="Choix Difficulté", font=("Arabic Transparent", 20))
titre.place(x=10,y=10, width = 200, height=50)

#fenetre fils ia noob
frameButtonIAnoob = Frame(root)
frameButtonIAnoob.place(x=350,y=75,width=300,height=50)
ButtonIAnoob = Button(frameButtonIAnoob, font="Arial")
ButtonIAnoob.place(x=10,y=10, width = 200, height=50)
ButtonIAnoob.config(text="Niveau IA facile", bg="white", fg="green")

#fenetre fils ia moyen
frameButtonIAmoy = Frame(root)
frameButtonIAmoy.place(x=350,y=125,width=300,height=50)
ButtonIAmoy = Button(frameButtonIAmoy, font="Arial")
ButtonIAmoy.place(x=10,y=10, width = 200, height=50)
ButtonIAmoy.config(text="Niveau IA moyenne", bg="white", fg="orange")

#fenetre fils ia difficile
frameButtonIAdiff = Frame(root)
frameButtonIAdiff.place(x=350,y=175,width=300,height=50)
ButtonIAdiff = Button(frameButtonIAdiff, font="Arial")
ButtonIAdiff.place(x=10,y=10, width = 200, height=50)
ButtonIAdiff.config(text="Niveau IA difficile", bg="white", fg="red")

# Créarion d'une fenêtre fils avec frame pour afficher le bouton de réinitialisation
frameBoutonReini = Frame(root)
frameBoutonReini.place(x=350,y=300,width=300,height=50)
boutonReinit = Button(frameBoutonReini, font=("Arial", 18), command= reset)
boutonReinit.place(x=10,y=10, width = 200, height=50)
boutonReinit.config(text="Réinitialiser")

#creation de la fenetre principale et personnalisation

root.title("Morpion")
root.minsize(500, 500)

# Lancement du jeu
game()

root.mainloop()

################### Jeu partie graphique ##############################