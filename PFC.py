from random import *

points_joueur = 0
points_ordinateur = 0

def regle():
    print("La Pierre bat les Ciseaux")
    print("La Feuille bat la Pierre")
    print("Les Ciseaux battent la Feuille")
    print("Si vous et l'ordinateur avez le même objet")
    print("Alors il y a égalite")
    print("Et le premier a 10 remporte la partie")


def choix_joueur(joueur): 
    joueur = input("pierre\npapier\nciseaux\n")
    while joueur not in ["pierre","papier","ciseaux"]:
        joueur = input("pierre\npapier\nciseaux\n")
    return(joueur)

def choix_ordinateur(nb, ordi):
    nb = randint(1,3)
    if nb == 1:   
        ordi = "pierre"
    elif nb == 2:
        ordi = "papier"
    else:
        ordi = "ciseaux"
    return(ordi)


print(choix_ordinateur)

if choix_joueur == "pierre" and choix_ordinateur == "ciseaux":
    print("Vous gagnez 1 point.")
    points_joueur = points_joueur + 1
elif choix_joueur == "pierre" and choix_ordinateur == "papier":
    print("L'ordinateur remporte 1 point.")
    points_ordinateur = points_ordinateur + 1
elif choix_joueur == "pierre" and choix_ordinateur == "pierre":
    print("Dommage égalité.")

if choix_joueur == "papier" and choix_ordinateur == "pierre":
    print("Vous gagnez 1 point.")
    points_joueur = points_joueur + 1
elif choix_joueur == "papier" and choix_ordinateur == "ciseaux":
    print("L'ordinateur remporte 1 point.")
    points_ordinateur = points_ordinateur + 1
elif choix_joueur == "papier" and choix_ordinateur == "papier":
    print("Dommage égalité.")

if choix_joueur == "ciseaux" and choix_ordinateur == "papier":
    print("Vous gagnez 1 point.")
    points_joueur = points_joueur + 1
elif choix_joueur == "ciseaux" and choix_ordinateur == "pierre":
    print("L'ordinateur remporte 1 point.")
    points_ordinateur = points_ordinateur + 1
elif choix_joueur == "ciseaux" and choix_ordinateur == "ciseaux":
    print("Dommage égalité.")

if points_ordinateur == 10:
    print("Dommage le résultat est de", points_ordinateur, "à", points_joueur)
elif points_joueur == 10: 
    print("Bravo tu a gagné avec un score de", points_joueur, "à", points_ordinateur)
