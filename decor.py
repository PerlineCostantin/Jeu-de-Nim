# Costantin Perline et Zaoun Eya Groupe 1

from turtle import *
from math import *
from random import *
import time


# paramètres du décor
tracer(1, 0)
colormode(255)


# fonctions pour dessiner les différentes formes dont sont composés les éléments du décor


def deplacer(x, y, t): # pour changer la position du curseur de la tortue avant chaque nouveau dessin
    t.up()
    t.goto(x, y)
    t.down()


def dessineCarre(x, couleur, t): # fonction pour dessiner un carré colorié d'une certaine couleur
    t.color(couleur)
    t.begin_fill()
    for i in range(4): # un carré est un polygone à 4 cotés, on repéte les mêmes instructions 4 fois
        t.forward(2 *x) 
        t.right(90)
    t.end_fill()


def dessineRectangle(l, L, couleur, x, y, t): # fonction pour dessiner un rectangle colorié d'une certaine couleur
    t.fillcolor(couleur)
    deplacer(x, y, t)
    t.begin_fill()
    for i in range(2): # on répète 2 fois les instructions
        t.left(90) # angle droit
        t.forward(L) # avancer de la largeur L
        t.left(90)
        t.forward(l) # avancer le la longueur l
    t.end_fill()


def sable(a1, a2, couleur, t):  # ligne entre mer et sable (fonction qui dessine une ligne brisée)
    t.color(couleur)
    t.begin_fill()
    t.left(90)
    t.forward(40)
    t.right(103)
    for i in range (0, 1500, 120):# i allant de 0 à 1500 en augmentant de 120 à chaque passage
        t.left(a1) # tourne à gauche de l'angle a1
        t.forward(60)
        t.right(a2) # tourne à droite de l'angle a2
        t.forward(60)
    t.right(95)
    t.forward(120)
    t.end_fill()


def dessineTriangle(x,y,l,t): # fonction pour dessiner un triangle 
    for i in range (3): # un triangle est un polygone à 3 cotés, on repéte les mêmes instructions 3 fois
        t.forward(l)
        t.right(120) # on tourne de 120 degrés car 360/3 = 120


def dessineDemiCercle(rayon, arc, couleur, x, y, t): # fonction pour dessiner un demi-cercle colorié d'une certaine couleur
    t.color(couleur)
    deplacer(x, y, t)
    t.begin_fill()
    t.right(270)
    t.circle(rayon, arc)
    t.end_fill()




# fonctions pour dessiner les différents éléments du décor


def dessineSoleil(rayon, arc, x, y, t):
    dessineDemiCercle(rayon, arc, "yellow", x, y, t) # appel de la fonction qui dessine un demi-cercle


def dessineEtoile(x, y, l, couleur, t): # fonction pour dessiner une étoile coloriée d'une certaine couleur
    deplacer(x, y, t)
    t.fillcolor(couleur)# la couleur du contour est la même que celle du remplissage
    t.color(couleur)
    t.begin_fill()
    for i in range(5): # on repète 5 fois les mêmes instructions
        t.forward(l) # avancer d'une longueur l
        t.right(144) 
    t.end_fill()


def random_color(): # fonction pour générer des couleurs aléatoires (on génère aléatoirement la nuance de rouge, de vert et de bleu)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def dessinePoisson(x,y,l,color,t): # fonction pour dessiner un poisson colorié d'une couleur aléatoire
    t.fillcolor(random_color())
    deplacer(x,y,t)
    t.begin_fill()
    t.setheading(135)
    # corps du poisson (deux demi-cerlces)
    t.circle(2*l,90)
    t.left(90)
    t.circle(2*l,90)
    t.setheading(30)
    # queue du poisson (un triangle)
    dessineTriangle(x,y,l,t)
    t.end_fill()


def dessineEcume(t):
    t.color("grey")
    t.fillcolor("white")
    for i in range(50): # trace 50 petits cercles 
        x=randint(-700,700) # x est choisi aléatoirement entre -700 et 700
        y=randint(-140,-100) # y est choisi aléatoirement entre -140 et -100
        deplacer(x,y,t)
        t.begin_fill()
        t.circle(randint(1,8))# le rayon du cercle est choisi aléatoirement entre 1 et 8
        t.end_fill()


def dessineServietteDePlage(l,L,x,y,t): # fonction pour dessiner une serviette de plage (composé de 4 rectangle)
    # les couleurs 1 et 2 sont tirées aléatoirement
    couleur1=random_color() 
    couleur2=random_color()
    t.setheading(0)
    t.width(3)# on augmente l'épaisseur du trait
    t.color("white")# couleur des countours en blanc
    # desssine 4 bandes verticales (4rectangles côte à côte) avec une alternance de couleurs
    dessineRectangle(l,L,couleur1,x,y,t)
    dessineRectangle(l,L,couleur2,x+l,y,t)
    dessineRectangle(l,L,couleur1,x+2*l,y,t)
    dessineRectangle(l,L,couleur2,x+3*l,y,t)


def dessinePetitNuage(x, y, couleur, taille, t): # fonction pour dessiner un petit nuage (composé de 6 demi-cercles)
    t.setheading(90)
    deplacer(x, y, t)
    t.width(1)
    t.color(couleur)
    t.fillcolor("white")
    t.begin_fill()
    # on tourne tout d'abord de 180 pour faire 2 demi-cercles côte à côte (haut du nuage)
    # puis de 90 pour faire l'extrémité gauche du nuage
    # puis encore de 90 pour faire le bas
    # puis de 180 pour faire un second demi-cerlce à coté
    # et enfin de 90 pour l'extrémité gauche 
    for angle in [180, 90, 90, 180, 90, 0]: # liste avec les angles dans l'orde (voir ci-dessus)
        t.circle(taille, 180) # dessine un demi-cercle
        t.right(angle) 
    t.end_fill()


def dessineGrosNuage(x, y, couleur, taille, t): # fonction pour dessiner un gros nuage (composé de 8 demi-cercles)
     t.setheading(90)
     deplacer(x, y, t)
     t.width(1)
     t.color(couleur)
     t.fillcolor("white")
     t.begin_fill()
     for j in range(2): # on repète le bloc ci-dessous 2 fois
         for i in range(2): # demi-cercles côte à côte
             t.circle(taille, 180)
             t.right(180)
         for i in range(2): # extrémité du nuage puis on revient (pour faire la ligne de demi-cercles du bas)
             t.circle(taille, 180)
             t.right(90)
     t.end_fill()
     

def petale(x, y, l, t): # fonction pour dessiner les pétales (2 demi-cercles qui se rejoignent)
    deplacer(x, y, t)
    t.begin_fill()
    t.fillcolor("pink")
    t.circle(l, 90) # premier demi-cercle
    t.left(90) # on tourne de 90 pour que les demi-cerlces se rejoignent
    t.circle(l, 90) # deuxième demi-cercle
    t.end_fill()


def dessineFleur(x, y, l, couleur, n, t): # fonction pour dessiner une fleur composée de n pétales
    t.color(couleur)
    for i in range(n):
        petale(x, y, l, t)
        t.left(((n*90)-360)/n)
        


def dessineFeuilles(nbFeuilles, rayon, arc, x, y, t): # fonction pour dessiner les feuilles de palmier
    deplacer(x, y, t)
    for i in range(nbFeuilles): # boucle pour dessiner le nombre de feuilles choisi
        dessineDemiCercle(rayon, arc, "green", x, y, t) # dessine à chaque fois une feuille (2 demis-cercles)
    dessineFleur(x - 10, y - 10, 10, "black", 5, t)
    dessineFleur(x + 10, y + 10, 10, "black", 5, t)


def dessinePalmier(x, y, t): # fonction pour dessiner un palmier
    t.color("black")
    dessineRectangle(20, 200, "darkgoldenrod", x, y, t)
    t.color("green")
    dessineFeuilles(5, 40, 120, x + 6, y, t)


def dessineVoileMat(x, y, c, t):  # fonction pour dessiner un triangle équilatéral (=les voiles) et sa hauteur(=le mat)
    # voiles et mat
    deplacer(x, y, t)
    t.color("black")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(3):
        t.forward(c)
        t.left(120)
    t.end_fill()
    deplacer(x - (c / 2), y, t)
    t.setheading(90)
    t.width(2)
    t.forward((sqrt(3) / 2) * c)
    t.up()


def dessineCoque(x, y, l, couleur, t): # fonction pour dessiner la coque 
    deplacer(x, y, t)
    t.fillcolor(couleur)
    t.begin_fill()
    t.right(45)
    t.forward(l)
    t.left(45)
    t.forward(2.5 * l)
    t.left(45)
    t.forward(l)
    t.end_fill()


def dessineBateau(x, y, l, casse, t): # fonction pour dessiner que la coque (si casse = True) ou le voilier entier (si casse = False)
    t.setheading(0)
    if not casse :
        # coque
        dessineCoque(x, y, l, "saddlebrown", t)
        # voiles et mat
        deplacer(x + (0.5 * x), y, t)
        t.setheading(120)
        dessineVoileMat(x + (3.4 * l), y, l * 3, t)
    else:
        dessineCoque(x, y, l, "saddlebrown", t)




# fonctions pour l'affichage textuel de la progression du jeu


def afficheScore(texte, t): # fonction pour afficher le nombre d'allumettes restantes
    deplacer(20, 205, t)# deplacer pour afficher le message dans le soleil
    t.write(texte, move=False, align="center", font=("Time New Roman", 14,"bold","italic"))# écrire le message centré, en police Times New Roman, de grosseur 14, en gras et en italique
    time.sleep(2) # on laisse le message affiché 2 secondes
    t.clear() # à chaque coup, le nombre d'allumettes restantes change donc on efface l'ancien message avec la fonction clear ete on réécrit le message avec le nombre d'allumettes mis à jour


def afficheAllumettesEnlevees(texte, t):# fonction pour afficher le nombre d'allumettes que le joueur ou l'ordinateur enlève
    deplacer(435, 270, t)# déplacer pour afficher le message dans le gros nuage
    t.write(texte, move=False, align="center", font=("Arial", 9))# écrire le message centré, en police Arial, de grosseur 9
    time.sleep(2) # on laisse le message affiché 2 secondes
    t.clear()# à chaque coup, le nombre d'allumettes enlevées change donc on efface l'ancien message avec la fonction clear ete on réécrit le nombre d'allumettes choisit par le joueur  ou l'ordinateur




# fonction pour dessiner tout le décor


def decor(t):
    x = window_width() 
    bgcolor('azure')# couleur de l'arrière plan
    deplacer(-x, 150, t)
    dessineCarre(x, 'lightskyblue', t)# pour dessiner la mer
    deplacer(-x, -130, t)
    dessineCarre(x, 'burlywood', t)# pour dessiner la plage
    sable(12, 10.8, 'burlywood', t)# pour dessiner la forme entre la mer et la plage
    deplacer(0, 0, t)
    t.left(90)
    dessineSoleil(150, 185, 160, 150, t)# pour dessiner le soleil
    # on dessine trois lignes d'étoiles de mer espacées régulièrement sur la plage
    for x in range(-400, 450, 200): # les étoiles sont espacées de 200
        dessineEtoile(x, -150, 40, "salmon", t)
    for x in range(-300, 350, 200):
        dessineEtoile(x, -250, 40, "coral", t)
    for x in range(-400, 450, 200):
        dessineEtoile(x, -350, 40, "tomato", t)
    dessineEcume(t) # on dessine les bulles d'écume
    t.right(93.3)# remettre la tortue en position 
    dessinePalmier(-500, -100, t)
    t.left(31)
    dessinePalmier(500, -100, t)
    t.setheading(0)
    # on dessine deux lignes de poissons
    for x in range(-440,490,170): # les poissons sont espacés de 170
        dessinePoisson(x,50,20,color,t)
    for x in range(-340,390,170):
        dessinePoisson(x,-55,23,color,t)
    # on dessine deux serviettes de plage sur le sable
    for x in range(-680,661,1340): # les serviettes sont espacées de 1340
        dessineServietteDePlage(20,120,x,-320,t)
    # on dessine des petits nuages
    for x in range (-500,-299,200):# pour dessiner 5 petits nuages en haut à gauche de la fenêtre
        dessinePetitNuage(x, 320, "black", 15, t)
    for x in range (-600,-199,200):
        dessinePetitNuage(x, 280, "black", 15, t)
    # pour dessiner 3 autres petits nuages en haut à droite de la fenêtre
    dessinePetitNuage(600, 350, "black", 15, t)
    dessinePetitNuage(300, 340, "black", 15, t)
    dessinePetitNuage(690, 280, "black", 15, t)
    # on dessine un gros nuage
    dessineGrosNuage(500, 300, "black", 23, t)

    
 
