# Costantin Perline et Zaoun Eya Groupe 1

from turtle import *
from math import *
from random import *
import time
from decor import * # on importe le module decor qui va dessiner le decor (fichier decor.py)


# on appelle une seule fois la fonction pour dessiner tout les bateaux, et pendant qu'on dessine, on va tester si c'est le moment de
# dessiner des bateaux cassé (par rapport au nombre total d'allumettes et le nombre restant)


def dessineAllumettes(nbreAllumettesTotal, nbreAllumettesRestantes, x, y, l, t):
    # Pour i allant de 0 jusqu'au nombre d'allumettes total exclus.
    for i in range(nbreAllumettesTotal):
        # Pour les 7 premiers bateaux (quand i vaut 0, 1, 2, 3, 4, 5 et 6):
        if i < 7:
            # On part de x et on ajoute une fois le nombre de bateaux affichés, donc pour le premier ça fait x + 0 * l = x
            # comme dans le premier if de la fonction ci-dessus, puis x + 1 * l etc...
            # teste directement quand on appelle la fonction si on a dépassé le nombre de bateaux pas cassés 
            dessineBateau(x + i * l, y, 30, i > nbreAllumettesRestantes-1, t)
        else:
            # On enlève 7 à i à partir du 8ème bateau (donc quand i vaut 7 puis 8 etc.)
            dessineBateau(x + (i-7) * l, y - 120, 30, i > nbreAllumettesRestantes-1, t)
       


# fonction pour le tour du joueur
def tourJoueur(choixJoueur, regle, allumettes):
    # tant que le nombre donné est hors de la règle ou inférieur au nombre d'allumettes disponible, on redemande au joueur de donner un nombre
    while not (choixJoueur in regle) or (choixJoueur > allumettes):
        choixJoueur = int(numinput("tentative", "erreur, choisissez un nombre plus petit ou un nombre dans la règle : ")) # la fonction numinput fait apparaître une fenêtre pop-up où le joueur peut rentrer un nombre entier
    afficheAllumettesEnlevees("Le joueur enlève " + str(choixJoueur) + " allumette(s)", t)# on affche sur le décor le choix du joueur
    # mise à jour du nombre d'allumettes
    allumettes = allumettes - choixJoueur 
    return allumettes


# fonction pour le tour de l'ordinateur
def tourOrdinateur(choixOrdinateur, regle, allumettes):
    print("Au tour de l'ordinateur de jouer")
    # tant que le nombre donné est inférieur au nombre d'allumettes disponible, on redemande à l'ordinateur de donner un nombre
    while choixOrdinateur > allumettes:
        choixOrdinateur = choice(regle) # l'ordinateur choisit un nombre qui fait partie de la liste qui constitue la règle
    afficheAllumettesEnlevees("L'ordinateur enlève " + str(choixOrdinateur) + " allumette(s)", t)# on affche sur le décor le choix de l'ordinateur
    # mise à jour du nombre d'allumettes
    allumettes = allumettes - choixOrdinateur
    print("L'ordinateur enlève", choixOrdinateur, "allumettes")
    return allumettes

def mex(l):
    #l2=l
    #l2.sort()
    #"for i in range (0,len(l2)):
        #if i<l2[i]:
            #return i
    #return len(l2)
    
    i=0
    while i in l:
        i+=1
    return i

def valPileAllumettes(n,regle):
    val=[0]
    for i in range (1,n+1):
        l=[]
        for j in regle:
            if i-j>=0:
                l.append(val[i-j])
        val.append(mex(l))
    return val[n]

def valJeuAllumettes(n,r):
    #l=[0]
    #if n==[]:
        #return 0
    #for i in n:
        #for j in range (1,i+1):
            #a=valPileAllumettes(j,r)
            #res=sumNimXOR(a,l[j-1])
            #l.append(res)
    #return res
    
    res=0
    for i in range (0,n):
        res^=valPileAllumettes(i,r)
    return res

        
                    
# initialisation des différentes tortues
t=Turtle()
tc=Turtle()
td=Turtle()
# pour cacher les tortues (curseurs)
hideturtle()
tc.hideturtle()
td.hideturtle()
t.hideturtle()


decor(td)# Affichage du décor

# mise en place des paramètres du jeu
regle = [1, 2, 3]  # choix de la règle
allumettes = 14 # tirage du nombre initial d'allumettes par l'ordinateur compris entre 4 et 15
choixOrdinateur = choice(regle)  # tire un nombre aléatoire allumettes
gagnant = False # initialisation de la variable gagnant : au départ du jeu il n'y a pas de gagnant
afficheScore("Nombre initial d'allumettes = " + str(allumettes), t)#affiche le nombre d'allumettes initial dans le soleil
print("Il y a", allumettes, "allumettes")# affiche le nombre d'allumettes initial dans le script

dessineAllumettes(allumettes, allumettes, -580, 120, 170, tc)# dessine les allumettes(bateaux)dans leur forme initiale et selon le nombre tiré au départ

a = allumettes

# on joue tant qu'il n'y a pas de gagnant
while not gagnant:
    val =valJeuAllumettes(allumettes, regle)
    if val==0:
        print("à vous de jouer")
        # on demande au joueur de donner un nombre d'allumettes dans une fenêtre pop-up directement sur l'interface
        choixJoueur = int(numinput("tentative", "donnez un nombre d'allumettes : ", default=None, minval=None, maxval=None))
        a = tourJoueur(choixJoueur, regle, a)
        time.sleep(2)
        tc.clear()
    
        # on redessine le même nombre d'allumettes en modifiant la forme des allumettes enlevées (le joueur choisit n allumettes qui seront redessinées de façon différente)
        dessineAllumettes(allumettes, a, -580, 120, 170, tc)


        print("Il reste", a, "allumettes")
        afficheScore("Allumettes restantes = " + str(a), t)
    
        # s'il reste 0 allumettes après le tour du joueur
        if a == 0 or a<min(regle):
            # il y a un gagnant (le joueur) donc la variable gagnant prend la valeur True
            gagnant = True
            # messages affichés dans le décor 
            afficheScore("Le joueur a gagné", t)# c'est le joueur qui gagne dans ce cas
            afficheScore("Fin de la partie", t)
            # messages affichés dans le script
            print("Vous avez gagné")
            print("Fin de la partie")

           # dans le cas contraire (s'il reste encore des allumettes)
        else:
            # au tour de l'ordinateur de jouer
            a = tourOrdinateur(choixOrdinateur, regle, a)
            time.sleep(2) # on attend 2 secondes

            tc.clear() # on efface les allumettes

            dessineAllumettes(allumettes, a, -580, 120, 170, tc) # on redessine les allumettes en adaptant leur forme

            afficheScore("Allumettes restantes = " + str(a), t) # affiche dans le décor le nombre d'allumettes restantes
        
            # s'il reste 0 allumettes après le tour de l'ordinateur
            if a == 0 or a<min(regle):
                # il y a un gagnant (l'ordinateur) donc la variable gagnant prend la valeur True
                gagnant = True
                # messages affichés dans le décor 
                afficheScore("L'ordinateur a gagné", t)
                afficheScore("Fin de la partie", t)
                # messages affichés dans le script
                print("L'ordinateur a gagné")
                print("Fin de la partie")

                # dans le cas contraire (s'il reste encore des allumettes)
            else:
                print("Il reste", a, "allumettes")
            
               # on repart au départ de la boucle

    else:
        print ("l'ordinateur joue")
        # s'il reste 0 allumettes après le tour du joueur
        if a == 0 or a<min(regle):
            # il y a un gagnant (le joueur) donc la variable gagnant prend la valeur True
            gagnant = True
            # messages affichés dans le décor 
            afficheScore("Le joueur a gagné", t)# c'est le joueur qui gagne dans ce cas
            afficheScore("Fin de la partie", t)
            # messages affichés dans le script
            print("Vous avez gagné")
            print("Fin de la partie")

           # dans le cas contraire (s'il reste encore des allumettes)
        else:
            # au tour de l'ordinateur de jouer
            a = tourOrdinateur(choixOrdinateur, regle, a)
            time.sleep(2) # on attend 2 secondes
    
            tc.clear() # on efface les allumettes

            dessineAllumettes(allumettes, a, -580, 120, 170, tc) # on redessine les allumettes en adaptant leur forme

            afficheScore("Allumettes restantes = " + str(a), t) # affiche dans le décor le nombre d'allumettes restantes
        
            # s'il reste 0 allumettes après le tour de l'ordinateur
            if a == 0 or a<min(regle):
                # il y a un gagnant (l'ordinateur) donc la variable gagnant prend la valeur True
                gagnant = True
                # messages affichés dans le décor 
                afficheScore("L'ordinateur a gagné", t)
                afficheScore("Fin de la partie", t)
                # messages affichés dans le script
                print("L'ordinateur a gagné")
                print("Fin de la partie")

                # dans le cas contraire (s'il reste encore des allumettes)
            else:
                print("Il reste", a, "allumettes")
                # on demande au joueur de donner un nombre d'allumettes dans une fenêtre pop-up directement sur l'interface
                choixJoueur = int(numinput("tentative", "donnez un nombre d'allumettes : ", default=None, minval=None, maxval=None))
                a = tourJoueur(choixJoueur, regle, a)
                time.sleep(2)
                tc.clear()
    
                # on redessine le même nombre d'allumettes en modifiant la forme des allumettes enlevées (le joueur choisit n allumettes qui seront redessinées de façon différente)
                dessineAllumettes(allumettes, a, -580, 120, 170, tc)


                print("Il reste", a, "allumettes")
                afficheScore("Allumettes restantes = " + str(a), t)
            
               # on repart au départ de la boucle
        
# à la fin de la partie
afficheScore("A bientot :)", t) # message affiché dans le décor
print("A bientôt :)") # message affiché dans le script
