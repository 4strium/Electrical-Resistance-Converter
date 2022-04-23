
# Auteur : Romain MELLAZA
# Date : 18-19-20-21-22/04/2022
# Description : Logiciel codé en Python qui permet à l'utilisateur (via une interface graphique) d'obtenir les couleurs des anneaux d'une résitance
# électrique et inversement.

# Importation de modules externes :
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

# Je défini ma fenêtre parent que j'appellerai "root" (ce sera mon accueil) :
root = Tk()

# Je défini des paramètres à cette fenêtre :
root.title("Convertisseur valeurs/couleurs des résistances électriques par Romain MELLAZA")     # Un titre
root.geometry("1080x720")                                                                       # Un resolution d'affichage, ici HD
root.minsize(1080, 720)                                                                         # Je bloque cette resolution, pour éviter que l'utilisateur ne redimmensionne n'importe comment.
root.maxsize(1080, 720)
root.iconbitmap(default='icon\LOGO_resistance.ico')                                             # Je défini un icon pour la fenêtre

# Je défini des variables essentielles avec leurs valeurs par défaut :

count_window_open = 0           # Compteur qui permet au programme de savoir combien de fenêtre l'utilisateur a ouvert !

# Constantes :
VALEUR_ANNEAU_1 = [             # Liste contenant toutes les valeurs possibles pour le premier anneau d'une resistance.
    # 0 impossible              # Ici il s'agit donc du premier chiffre significatif.
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

VALEUR_ANNEAU_2 = [             # Liste contenant toutes les valeurs possibles pour le second anneau d'une resistance.
    "0",                        # Ici il s'agit donc du second chiffre significatif.
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

VALEUR_ANNEAU_3 = [           # Liste contenant toutes les valeurs possibles pour le troisième anneau d'une resistance.  
    "0",                      # Ici il s'agit donc du troisième chiffre significatif.
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "Aucun" # Possibilité de ne pas avoir de 3ème chiffre significatif.
]

VALEUR_MULTIPLI = [           # Liste contenant toutes les valeurs possibles pour le quatrième anneau d'une resistance.
    "x1",                     # Ici il s'agit donc du multiplicateur.
    "x10",
    "x100",
    "x1k",
    "x10k",
    "x100k",
    "x1M",
    "x10M",
    "x100M",
    "x1G",
    "x0.1",
    "x0.01"
]

VALEUR_TOLERANCE = [        # Liste contenant toutes les valeurs possibles pour le cinquième anneau d'une resistance.
    "±10%",                 # Ici il s'agit donc des valeurs de tolérance.
    "±5%",
    "±2%",
    "±1%",
    "±0.5%",
    "±0.25%",
    "±0.10%"
]

VALEUR_TEMPERATURE = [      # Liste contenant toutes les valeurs possibles pour le sixième anneau d'une resistance.
    "250ppm/K",             # Ici il s'agit donc des coefficients de témpérature.
    "100ppm/K",
    "50ppm/K",
    "25ppm/K",
    "20ppm/K",
    "15ppm/K",
    "10ppm/K",
    "5ppm/K",
    "1ppm/K",
    "Aucun"  # Possibilité de ne pas avoir de coefficient de température indiqué.
]

COULEUR_ANNEAU_1 = [        # Liste contenant toutes les couleurs possibles pour le premier anneau d'une resistance.
    "Marron",
    "Rouge",
    "Orange",
    "Jaune",
    "Vert",
    "Bleu",
    "Violet",
    "Gris",
    "Blanc"
]

COULEUR_ANNEAU_2 = [        # Liste contenant toutes les couleurs possibles pour le deuxième anneau d'une resistance.
    "Noir",     # Possibilité que le deuxième chiffre significatif soit égal à 0.
    "Marron",
    "Rouge",
    "Orange",
    "Jaune",
    "Vert",
    "Bleu",
    "Violet",
    "Gris",
    "Blanc"
]

COULEUR_ANNEAU_3 = [        # Liste contenant toutes les couleurs possibles pour le troisième anneau d'une resistance.
    "Noir",
    "Marron",
    "Rouge",
    "Orange",
    "Jaune",
    "Vert",
    "Bleu",
    "Violet",
    "Gris",
    "Blanc",
    "Il n'y en a pas !"   # Possibilité de ne pas avoir de 3ème chiffre significatif.
]

COULEUR_ANNEAU_4 = [        # Liste contenant toutes les couleurs possibles pour le quatrième anneau d'une resistance.
    "Noir",
    "Marron",
    "Rouge",
    "Orange",
    "Jaune",
    "Vert",
    "Bleu",
    "Violet",
    "Gris",
    "Blanc",
    "Or",
    "Argent"
]

COULEUR_ANNEAU_5 = [        # Liste contenant toutes les couleurs possibles pour le cinquième anneau d'une resistance.
    "Marron",
    "Rouge",
    "Vert",
    "Bleu",
    "Violet",
    "Or",
    "Argent"
]

COULEUR_ANNEAU_6 = [        # Liste contenant toutes les couleurs possibles pour le sixième anneau d'une resistance.
    "Noir",
    "Marron",
    "Rouge",
    "Orange",
    "Jaune",
    "Bleu",
    "Violet",
    "Gris",
    "Il n'y en a pas !"  # Possibilité de ne pas avoir de coefficient de température indiqué.
]

##############################################################################################################################################################################################################
#                                                                                     ACCUEIL                                                                                                                #
#                                                                                                                                                                                                            #

# J'importe et j'affiche une image de fond pour mon accueil :
bg = PhotoImage(file = "img\Background_IMAGE.png")
canvas_accueil = Canvas( root, width = 1080, height = 720)
canvas_accueil.pack(fill = "both", expand = True)
canvas_accueil.create_image( 0, 0, image = bg, anchor = "nw")

# J'affiche un titre sur ma page d'accueil :
i=canvas_accueil.create_text(540.45, 137, text=' Bienvenue dans le convertisseur \n de résistance électrique ! ', font=("Helvetica", 42), fill="white", justify = CENTER)
r=canvas_accueil.create_rectangle(canvas_accueil.bbox(i),fill="#feb58a", width = 1)                                                            
canvas_accueil.tag_lower(r,i)

# J'affiche une question pour l'utilisateur :
k=canvas_accueil.create_text(540.45, 310, text=' Quelle conversion voulez-vous réaliser ? ', font=("Helvetica", 35), fill="white")
l=canvas_accueil.create_rectangle(canvas_accueil.bbox(k),fill="#feb58a", width = 1)
canvas_accueil.tag_lower(l,k)



##############################################################################################################################################################################################################
#                                                                                 MODE VALEUR ➔ COULEUR                                                                                                     #
#                                                                                                                                                                                                            #


def image_converter(root_correspondant, canvas_correspondant, ring1, ring2, ring3, ring4, ring5, ring6):
    '''
    Fonction complexe qui affiche les images d'anneaux de couleurs en fonction de ce que l'utilisateur a fourni comme donnée  pour chaque anneaux (ring1, ring2, ...), 
    ce sont donc ces variables en paramètres. Il y a aussi la racine et la toile pour que le programme sache où il doit afficher les anneaux de couleurs.
    '''
    global flèche_temporaire_1, flèche_temporaire_2

    # J'affiche mon image de resistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_correspondant.create_image(50, 170, image = image_resistance_vide, anchor='nw')

    # J'affiche une flèche allant du sélecteur du premier chiffre significatif à l'anneau correspondant :
    image_flèche_1 = ImageTk.PhotoImage(file = "img/arrows/first.png")
    canvas_correspondant.create_image(80, 148, image = image_flèche_1, anchor='nw')

    # J'affiche une flèche allant du sélecteur du second chiffre significatif à l'anneau correspondant :
    image_flèche_2 = ImageTk.PhotoImage(file = "img/arrows/second.png")
    canvas_correspondant.create_image(306, 155, image = image_flèche_2, anchor='nw')

    # J'affiche une flèche allant du sélecteur du multiplicateur à l'anneau correspondant :
    image_flèche_4 = ImageTk.PhotoImage(file = "img/arrows/fourth.png")
    canvas_correspondant.create_image(420, 147, image = image_flèche_4, anchor='nw')

    # J'affiche une flèche allant du sélecteur de tolérance à l'anneau correspondant :
    image_flèche_5 = ImageTk.PhotoImage(file = "img/arrows/five.png")
    canvas_correspondant.create_image(540, 146, image = image_flèche_5, anchor='nw')

    # J'affiche une flèche allant du sélecteur du troisième chiffre significatif à l'anneau correspondant, SEULEMENT si il y en a un :
    if ring3.get() != 'Aucun' : 
        try : 
            canvas_correspondant.delete(flèche_temporaire_1)
            image_flèche_3 = ImageTk.PhotoImage(file = "img/arrows/third.png")
            flèche_temporaire_1 = canvas_correspondant.create_image(368, 153, image = image_flèche_3, anchor='nw')
        except : 
            image_flèche_3 = ImageTk.PhotoImage(file = "img/arrows/third.png")
            flèche_temporaire_1 = canvas_correspondant.create_image(368, 153, image = image_flèche_3, anchor='nw')
    else :
        # Sinon je supprime la flèche précédente :
        try :
            canvas_correspondant.delete(flèche_temporaire_1)
        except :
            pass

    # J'affiche une flèche allant du sélecteur du coefficient de température à l'anneau correspondant, SEULEMENT si il y en a un :
    if ring6.get() != 'Aucun' :
        try :
            canvas_correspondant.delete(flèche_temporaire_2)
            image_flèche_6 = ImageTk.PhotoImage(file = "img/arrows/six.png")
            flèche_temporaire_2 = canvas_correspondant.create_image(600, 450, image = image_flèche_6, anchor='nw')
        except :
            image_flèche_6 = ImageTk.PhotoImage(file = "img/arrows/six.png")
            flèche_temporaire_2 = canvas_correspondant.create_image(600, 450, image = image_flèche_6, anchor='nw')
    else :
        # Sinon je supprime la flèche précédente :
        try :
            canvas_correspondant.delete(flèche_temporaire_2)
        except :
            pass
    # A noter qu'ici j'ai utilisé la structure try...except car au démarrage il est bien entendu impossible de supprimer la flèche précédente, 
    # je fais donc comprendre au programme que ce n'est pas grave et qu'il peut passer à le suite !

    # En fonction de ce que l'utilisateur a sélectionné comme valeur pour le premier chiffre significatif j'affiche l'image de couleur correspondante :
    if ring1.get() == '1':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/brown.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '2':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/red.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '3':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/orange.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '4':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/yellow.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '5':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/green.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '6':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/blue.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '7':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '8':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/grey.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    elif ring1.get() == '9':
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/white.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau1, anchor='nw')
    
    # En fonction de ce que l'utilisateur a sélectionné comme valeur pour le second chiffre significatif j'affiche l'image de couleur correspondante :
    if ring2.get() == '0':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/black.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '1':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/brown.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '2':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/red.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '3':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/orange.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '4':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/yellow.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '5':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/green.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '6':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/blue.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '7':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '8':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/grey.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')
    elif ring2.get() == '9':
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/white.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau2, anchor='nw')

    # En fonction de ce que l'utilisateur a sélectionné comme valeur pour le troisième chiffre significatif j'affiche l'image de couleur correspondante :
    if ring3.get() == '0' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/black.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '1' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/brown.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '2' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/red.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '3' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/orange.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '4' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/yellow.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '5' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/green.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '6' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/blue.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '7' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '8' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/grey.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    elif ring3.get() == '9' :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/white.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau3, anchor='nw')
    
    # En fonction de ce que l'utilisateur a sélectionné comme valeur pour le multiplicateur j'affiche l'image de couleur correspondante :
    if ring4.get() == 'x1' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/black.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x10' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/brown.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x100' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/red.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x1k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/orange.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x10k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/yellow.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x100k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/green.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x1M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/blue.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x10M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x100M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/grey.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x1G' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/white.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x0.1' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/gold.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    elif ring4.get() == 'x0.01' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/silver.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau4, anchor='nw')
    
    # En fonction de ce que l'utilisateur a sélectionné comme valeur pour la tolérance j'affiche l'image de couleur correspondante :
    if ring5.get() == '±10%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/silver.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
    elif ring5.get() == '±5%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/gold.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
    elif ring5.get() == '±1%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/brown.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
    elif ring5.get() == '±2%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/red.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
    elif ring5.get() == '±0.5%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/green.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
    elif ring5.get() == '±0.25%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/blue.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
    elif ring5.get() == '±0.10%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')

    # En fonction de ce que l'utilisateur a sélectionné comme valeur pour le premier chiffre significatif j'affiche l'image de couleur correspondante :
    if ring6.get() == '250ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/black.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '100ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/brown.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '50ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/red.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '25ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/yellow.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '20ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/green.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '15ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/orange.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '10ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/blue.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '5ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')
    elif ring6.get() == '1ppm/K' :
        image_anneau6 = ImageTk.PhotoImage(file = "img/anneau_6/grey.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau6, anchor='nw')

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre ! 
    try:
        root_correspondant.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.


def spawn_selecteurs(root_correspondant, canvas_correspondant):
    '''
    Fonction complexe qui affiche les différents sélecteurs de valeurs possible pour chaque anneaux sur la page !
    Elle admet donc en paramètres la racine ainsi que la toile pour savoir où afficher les sélecteurs.
    '''

    # Je défini la variable qui permet de recueillir le choix de l'utilisateur pour le premier chiffre significatif :
    anneau1 = StringVar() # Il s'agit d'une chaîne de caractères.

    # Je passe à la variable une valeur par défaut, je choisi que ce sera la première valeur de la liste correspondante :
    anneau1.set(VALEUR_ANNEAU_1[0])

    # J'ai choisi d'utiliser des menus déroulant dans tout le logiciel pour éviter que l'utilisateur ne rentre n'importe quoi comme couleur ou valeur :
    drop_chiffre_1 = OptionMenu(root_correspondant, anneau1, *VALEUR_ANNEAU_1)

    # J'affecte des attributs graphiques au menu :
    drop_chiffre_1.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_1["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")

    # Je l'affiche à un endroit précis de la page :
    canvas_correspondant.create_window(50, 125, anchor='nw', window=drop_chiffre_1)
    a=canvas_correspondant.create_text(138, 85, text='1er\nchiffre significatif :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    b=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(a),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(b,a)

    # Je défini la variable qui permet de recueillir le choix de l'utilisateur pour le second chiffre significatif :
    anneau2 = StringVar() # Il s'agit d'une chaîne de caractères.

    # Je passe à la variable une valeur par défaut, je choisi que ce sera la première valeur de la liste correspondante :
    anneau2.set(VALEUR_ANNEAU_2[0])

    # J'ai choisi d'utiliser des menus déroulant dans tout le logiciel pour éviter que l'utilisateur ne rentre n'importe quoi comme couleur ou valeur :
    drop_chiffre_2 = OptionMenu(root_correspondant, anneau2, *VALEUR_ANNEAU_2)

    # J'affecte des attributs graphiques au menu :
    drop_chiffre_2.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_2["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")

    # Je l'affiche à un endroit précis de la page :
    canvas_correspondant.create_window(250, 125, anchor='nw', window=drop_chiffre_2)
    c=canvas_correspondant.create_text(338, 85, text='2ème\nchiffre significatif :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    d=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(c),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(d,c)

    # Je défini la variable qui permet de recueillir le choix de l'utilisateur pour le troisième chiffre significatif :
    anneau3 = StringVar() # Il s'agit d'une chaîne de caractères.

    # Je passe à la variable une valeur par défaut, je choisi que ce sera la onzième valeur de la liste correspondante :
    anneau3.set(VALEUR_ANNEAU_3[10])

    # J'ai choisi d'utiliser des menus déroulant dans tout le logiciel pour éviter que l'utilisateur ne rentre n'importe quoi comme couleur ou valeur :
    drop_chiffre_3 = OptionMenu(root_correspondant, anneau3, *VALEUR_ANNEAU_3)

    # J'affecte des attributs graphiques au menu :
    drop_chiffre_3.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_3["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")

    # Je l'affiche à un endroit précis de la page :
    canvas_correspondant.create_window(450, 125, anchor='nw', window=drop_chiffre_3)
    e=canvas_correspondant.create_text(538, 85, text='3ème\nchiffre significatif :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    f=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(e),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(f,e)

    # Je défini la variable qui permet de recueillir le choix de l'utilisateur pour le multiplicateur :
    anneau_multipli = StringVar() # Il s'agit d'une chaîne de caractères.

    # Je passe à la variable une valeur par défaut, je choisi que ce sera la première valeur de la liste correspondante :
    anneau_multipli.set(VALEUR_MULTIPLI[0])

    # J'ai choisi d'utiliser des menus déroulant dans tout le logiciel pour éviter que l'utilisateur ne rentre n'importe quoi comme couleur ou valeur :
    drop_chiffre_multipli = OptionMenu(root_correspondant, anneau_multipli, *VALEUR_MULTIPLI)

    # J'affecte des attributs graphiques au menu :
    drop_chiffre_multipli.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_multipli["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")

    # Je l'affiche à un endroit précis de la page :
    canvas_correspondant.create_window(650, 125, anchor='nw', window=drop_chiffre_multipli)
    g=canvas_correspondant.create_text(738, 85, text='Multiplicateur :\n', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    h=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(g),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(h,g)

    # Je défini la variable qui permet de recueillir le choix de l'utilisateur pour la tolérance :
    anneau_tolerance = StringVar()  # Il s'agit d'une chaîne de caractères.

    # Je passe à la variable une valeur par défaut, je choisi que ce sera la première valeur de la liste correspondante :
    anneau_tolerance.set(VALEUR_TOLERANCE[0])

    # J'ai choisi d'utiliser des menus déroulant dans tout le logiciel pour éviter que l'utilisateur ne rentre n'importe quoi comme couleur ou valeur :
    drop_chiffre_tolerance = OptionMenu(root_correspondant, anneau_tolerance, *VALEUR_TOLERANCE)

    # J'affecte des attributs graphiques au menu :
    drop_chiffre_tolerance.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_tolerance["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")

    # Je l'affiche à un endroit précis de la page :
    canvas_correspondant.create_window(850, 125, anchor='nw', window=drop_chiffre_tolerance)
    o=canvas_correspondant.create_text(938, 85, text='Tolérance :\n', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    p=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(o),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(p,o)

    # Je défini la variable qui permet de recueillir le choix de l'utilisateur pour le coefficient de température :
    anneau_temperature = StringVar()  # Il s'agit d'une chaîne de caractères.

    # Je passe à la variable une valeur par défaut, je choisi que ce sera la dixième valeur de la liste correspondante :
    anneau_temperature.set(VALEUR_TEMPERATURE[9])

    # J'ai choisi d'utiliser des menus déroulant dans tout le logiciel pour éviter que l'utilisateur ne rentre n'importe quoi comme couleur ou valeur :
    drop_chiffre_temperature = OptionMenu(root_correspondant, anneau_temperature, *VALEUR_TEMPERATURE)

    # J'affecte des attributs graphiques au menu :
    drop_chiffre_temperature.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_temperature["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")

    # Je l'affiche à un endroit précis de la page :
    canvas_correspondant.create_window(850, 650, anchor='nw', window=drop_chiffre_temperature)
    t=canvas_correspondant.create_text(938, 610, text='Coefficient\ntempérature :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    u=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(t),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(u,t)

    # Je défini et j'affiche un bouton pour valider les valeurs sélectionner par l'utilisateur :
    button_validation = Button(root_correspondant, text="Valider ✓", command=lambda *args: image_converter(root_correspondant, canvas_correspondant, anneau1, anneau2, anneau3, anneau_multipli, anneau_tolerance, anneau_temperature), font=("Helvetica", 18), fg='BLACK', bg="#feb58a", height = 2, width = 12)
    canvas_correspondant.create_window(870, 380, anchor='nw', window=button_validation)

    # On a vu cette fonction précedemment mais ici je l'apelle une seule fois pour afficher les valeurs par défaut et montrer à l'utilisateur ce qu'il peut faire !
    # Par la suite l'utilisateur pourra rappeler la fonction en appuyant sur le bouton de validation défini juste au dessus.
    image_converter(root_correspondant, canvas_correspondant, anneau1, anneau2, anneau3, anneau_multipli, anneau_tolerance, anneau_temperature)


def open_value_to_color():
    '''
    Cette procédure est appelée quand l'utilisateur appuie sur le bouton du mode "Valeur -> Couleur"
    Elle met en place la fenêtre avec des paramètres comme la résolution, le titre, ... SEULEMENT si cette fenêtre n'est pas déjà ouverte,
    sinon elle affiche un message d'avertissement à l'utilisateur !
    Puis elle crée une toile ("Canvas") pour la page.
    Ensuite les deux fonctions que l'on vient de voir prennent le relais. 
    '''
    global count_window_open, root_value_to_color
    if count_window_open == 0 :
        root_value_to_color = Toplevel(root)
        root_value_to_color.title("Convertisseur valeurs/couleurs des résistances électriques par Romain MELLAZA")
        root_value_to_color.geometry("1080x720")
        root_value_to_color.minsize(1080, 720)
        root_value_to_color.maxsize(1080, 720)
        canvas_value_to_color = Canvas( root_value_to_color, width = 1080, height = 720)
        canvas_value_to_color.pack(fill = "both", expand = True)
        bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_value_to_color.create_image( 0, 0, image = bg, anchor='nw')
        count_window_open += 1
        spawn_selecteurs(root_value_to_color, canvas_value_to_color)
    else :
        messagebox.showinfo("Erreur","Vous avez déjà ouvert une fenêtre de conversion !")





##############################################################################################################################################################################################################
#                                                                                 MODE COULEUR ➔ VALEUR                                                                                                     #
#                                                                                                                                                                                                            #


def color_converter_number_1_to_3(root_correspondant, ring, step):
    '''
    Fonction complexe qui remplie les varaibles de chaque anneaux en fonction de ce que l'utilisateur a choisi comme couleur pour l'anneau.
    J'admet donc en paramètres l'anneau ("ring"), l'étape ("step") pour savoir de quelle anneau il s'agit (1, 2, 3, ...) ainsi que la racine ("root_correspondant")
    pour ouvrir la fenêtre suivante qui permettra à l'utilisateur de choisir la couleur de l'anneau suivant !
    '''
    global chiffre_1, chiffre_2, chiffre_3, chiffre_4, chiffre_5, chiffre_6

    # Je vais expliquer le fonctionnement seulement pour la couleur Noir car pour les autres couleurs c'est strictement le même type de fonctionnement !
    # En premier lieu je vérifie de quelle couleur est l'anneau via la commande "ring.get()".
    if ring.get() == 'Noir' :

        # Puis je vérfie l'étape à l'aquelle l'utilisateur se trouve :
        # Cela me permet de remplir la bonne variable et donc la bonne valeur !
        if step == 2 :
            chiffre_2 = 0
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 0
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[0]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[0]
            open_color_to_value_result(root_correspondant)

    if ring.get() == 'Marron' :
        if step == 1 :
            chiffre_1 = 1
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 1
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 1
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[1]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[3]
            open_color_to_value_anneau_6(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[1]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Rouge' :
        if step == 1 :
            chiffre_1 = 2
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 2
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 2
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[2]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[2]
            open_color_to_value_anneau_6(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[2]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Orange' :
        if step == 1 :
            chiffre_1 = 3
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 3
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 3
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[3]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[5]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Jaune' :
        if step == 1 :
            chiffre_1 = 4
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 4
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 4
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[4]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[3]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Vert' :
        if step == 1 :
            chiffre_1 = 5
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 5
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 5
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[5]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[4]
            open_color_to_value_anneau_6(root_correspondant)
    if ring.get() == 'Bleu' :
        if step == 1 :
            chiffre_1 = 6
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 6
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 6
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[6]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[5]
            open_color_to_value_anneau_6(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[6]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Violet' :
        if step == 1 :
            chiffre_1 = 7
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 7
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 7
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[7]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[6]
            open_color_to_value_anneau_6(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[7]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Gris' :
        if step == 1 :
            chiffre_1 = 8
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 8
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 8
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[8]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 6 :
            chiffre_6 = VALEUR_TEMPERATURE[8]
            open_color_to_value_result(root_correspondant)
    if ring.get() == 'Blanc' :
        if step == 1 :
            chiffre_1 = 9
            open_color_to_value_anneau_2(root_correspondant)
        elif step == 2 :
            chiffre_2 = 9
            open_color_to_value_anneau_3(root_correspondant)
        elif step == 3 :
            chiffre_3 = 9
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[9]
            open_color_to_value_anneau_5(root_correspondant)  
    if ring.get() == 'Or' :
        if step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[10]
            open_color_to_value_anneau_5(root_correspondant)
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[1]
            open_color_to_value_anneau_6(root_correspondant)
    if ring.get() == 'Argent' :
        if step == 4 :
            chiffre_4 = VALEUR_MULTIPLI[11]
            open_color_to_value_anneau_5(root_correspondant) 
        elif step == 5 :
            chiffre_5 = VALEUR_TOLERANCE[0]
            open_color_to_value_anneau_6(root_correspondant)
    if ring.get() == "Il n'y en a pas !" :
        if step == 3 :
            chiffre_3 = None
            open_color_to_value_anneau_4(root_correspondant)
        elif step == 6 :
            chiffre_6 = None
            open_color_to_value_result(root_correspondant)



def spawn_selecteurs_part2(root_correspondant, canvas_correspondant, step):
    '''
    Fonction complexe qui affiche les différents sélecteurs de coueleurs possible pour chaque anneaux sur la page, en fonction de l'étape actuelle !
    Elle admet donc en paramètres l'étape ("step"), la racine ainsi que la toile pour savoir où afficher les sélecteurs.
    J'utilise la même logique que pour la fonction "spawn_selecteurs" de l'autre mode, elle contient plus de commentaire détaillés sur le fonctionnement ! 
    La seule différence est qu'ici chaque menu déroulant apparaît sur une fen^tre différente, je dois donc changer de menu en condition l'étape.
    '''
    if step == 1 :
        anneau1_part2 = StringVar()
        anneau1_part2.set(COULEUR_ANNEAU_1[0])
        drop_couleur_1 = OptionMenu(root_correspondant, anneau1_part2, *COULEUR_ANNEAU_1)
        drop_couleur_1.config(width = 10, font=("Helvetica", 25), fg ='white', bg="#feb58a", activebackground="#feb58a", activeforeground = 'white')
        drop_couleur_1["menu"].config(font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
        canvas_correspondant.create_window(220, 200, anchor='nw', window=drop_couleur_1)
        button_validation_couleur_1 = Button(root_correspondant, text="Valider ✓", command=lambda *args: color_converter_number_1_to_3(root_correspondant, anneau1_part2, step), font=("Helvetica", 25), fg='WHITE', bg="#feb58a", height = 1, width = 10)
        canvas_correspondant.create_window(575, 192, anchor='nw', window=button_validation_couleur_1)
    if step == 2 :
        anneau2_part2 = StringVar()
        anneau2_part2.set(COULEUR_ANNEAU_2[0])
        drop_couleur_2 = OptionMenu(root_correspondant, anneau2_part2, *COULEUR_ANNEAU_2)
        drop_couleur_2.config(width = 10, font=("Helvetica", 25), fg ='white', bg="#feb58a", activebackground="#feb58a", activeforeground = 'white')
        drop_couleur_2["menu"].config(font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
        canvas_correspondant.create_window(220, 200, anchor='nw', window=drop_couleur_2)
        button_validation_couleur_2 = Button(root_correspondant, text="Valider ✓", command=lambda *args: color_converter_number_1_to_3(root_correspondant, anneau2_part2, step), font=("Helvetica", 25), fg='WHITE', bg="#feb58a", height = 1, width = 10)
        canvas_correspondant.create_window(575, 192, anchor='nw', window=button_validation_couleur_2)
    if step == 3 :
        anneau3_part2 = StringVar()
        anneau3_part2.set(COULEUR_ANNEAU_3[10])
        drop_couleur_3 = OptionMenu(root_correspondant, anneau3_part2, *COULEUR_ANNEAU_3)
        drop_couleur_3.config(width = 14, font=("Helvetica", 25), fg ='white', bg="#feb58a", activebackground="#feb58a", activeforeground = 'white')
        drop_couleur_3["menu"].config(font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
        canvas_correspondant.create_window(220, 200, anchor='nw', window=drop_couleur_3)
        button_validation_couleur_3 = Button(root_correspondant, text="Valider ✓", command=lambda *args: color_converter_number_1_to_3(root_correspondant, anneau3_part2, step), font=("Helvetica", 25), fg='WHITE', bg="#feb58a", height = 1, width = 10)
        canvas_correspondant.create_window(575, 192, anchor='nw', window=button_validation_couleur_3)
    if step == 4 :
        anneau4_part2 = StringVar()
        anneau4_part2.set(COULEUR_ANNEAU_4[10])
        drop_couleur_4 = OptionMenu(root_correspondant, anneau4_part2, *COULEUR_ANNEAU_4)
        drop_couleur_4.config(width = 10, font=("Helvetica", 25), fg ='white', bg="#feb58a", activebackground="#feb58a", activeforeground = 'white')
        drop_couleur_4["menu"].config(font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
        canvas_correspondant.create_window(220, 200, anchor='nw', window=drop_couleur_4)
        button_validation_couleur_4 = Button(root_correspondant, text="Valider ✓", command=lambda *args: color_converter_number_1_to_3(root_correspondant, anneau4_part2, step), font=("Helvetica", 25), fg='WHITE', bg="#feb58a", height = 1, width = 10)
        canvas_correspondant.create_window(575, 192, anchor='nw', window=button_validation_couleur_4)
    if step == 5 :
        anneau5_part2 = StringVar()
        anneau5_part2.set(COULEUR_ANNEAU_5[6])
        drop_couleur_5 = OptionMenu(root_correspondant, anneau5_part2, *COULEUR_ANNEAU_5)
        drop_couleur_5.config(width = 10, font=("Helvetica", 25), fg ='white', bg="#feb58a", activebackground="#feb58a", activeforeground = 'white')
        drop_couleur_5["menu"].config(font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
        canvas_correspondant.create_window(220, 200, anchor='nw', window=drop_couleur_5)
        button_validation_couleur_5 = Button(root_correspondant, text="Valider ✓", command=lambda *args: color_converter_number_1_to_3(root_correspondant, anneau5_part2, step), font=("Helvetica", 25), fg='WHITE', bg="#feb58a", height = 1, width = 10)
        canvas_correspondant.create_window(575, 192, anchor='nw', window=button_validation_couleur_5)
    if step == 6 :
        anneau6_part2 = StringVar()
        anneau6_part2.set(COULEUR_ANNEAU_6[0])
        drop_couleur_6 = OptionMenu(root_correspondant, anneau6_part2, *COULEUR_ANNEAU_6)
        drop_couleur_6.config(width = 14, font=("Helvetica", 25), fg ='white', bg="#feb58a", activebackground="#feb58a", activeforeground = 'white')
        drop_couleur_6["menu"].config(font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
        canvas_correspondant.create_window(220, 200, anchor='nw', window=drop_couleur_6)
        button_validation_couleur_6 = Button(root_correspondant, text="Valider ✓", command=lambda *args: color_converter_number_1_to_3(root_correspondant, anneau6_part2, step), font=("Helvetica", 25), fg='WHITE', bg="#feb58a", height = 1, width = 10)
        canvas_correspondant.create_window(575, 192, anchor='nw', window=button_validation_couleur_6)





def clignotement(root_correspondant, canvas_correspondant, step_light):
    '''
    Fonction qui permet de faire clignoter un rond rouge pour indiquer l'anneau que l'utilisateur doit regarder dans la vraie vie.
    Cette fonction est couplée au fonction d'affichage et de supression que j'alterne à un certain rythme (500ms) afin de produire l'effet de clignotement.
    '''
    count = 0               # Définition du compteur de la boucle.
    chrono_x = 500          # Définition du compteur de millisecondes entre chaque suppression.
    chrono_y = 1000         # Définition du compteur de millisecondes entre chaque affichage.
    while count < 1000 :
        root_correspondant.after(chrono_x, lambda *args: suppr_image(canvas_correspondant, step_light))
        root_correspondant.after(chrono_y, lambda *args: display_image(canvas_correspondant, step_light))
        count += 1          # J'incrémente le compteur de la boucle.
        chrono_x += 1000    # J'incrémente de 1000ms le compteur de suppression.
        chrono_y += 1000    # J'incrémente de 1000ms le compteur d'affichage.

def suppr_image(canvas_correspondant, step_light):
    '''
    Fonction de suppression d'images.
    '''
    if step_light == 1:
        canvas_correspondant.delete(image_clignotant_ring_1_window)
    if step_light == 2:
        canvas_correspondant.delete(image_clignotant_ring_2_window)
    if step_light == 3:
        canvas_correspondant.delete(image_clignotant_ring_3_window)
    if step_light == 4:
        canvas_correspondant.delete(image_clignotant_ring_4_window)
    if step_light == 5:
        canvas_correspondant.delete(image_clignotant_ring_5_window)
    if step_light == 6:
        canvas_correspondant.delete(image_clignotant_ring_6_window)

def display_image(canvas_correspondant, step_light):
    '''
    Fonction d'affichage d'images.
    '''
    global image_clignotant_ring_1_window, image_clignotant_ring_2_window, image_clignotant_ring_3_window, image_clignotant_ring_4_window, image_clignotant_ring_5_window, image_clignotant_ring_6_window
    if step_light == 1:
        image_clignotant_ring_1_window = canvas_correspondant.create_image(145, 170, image = image_clignotant_ring_1, anchor='nw')
    if step_light == 2:
        image_clignotant_ring_2_window = canvas_correspondant.create_image(145, 170, image = image_clignotant_ring_2, anchor='nw')
    if step_light == 3:
        image_clignotant_ring_3_window = canvas_correspondant.create_image(145, 170, image = image_clignotant_ring_3, anchor='nw')
    if step_light == 4:
        image_clignotant_ring_4_window = canvas_correspondant.create_image(145, 170, image = image_clignotant_ring_4, anchor='nw')
    if step_light == 5:
        image_clignotant_ring_5_window = canvas_correspondant.create_image(145, 170, image = image_clignotant_ring_5, anchor='nw')
    if step_light == 6:
        image_clignotant_ring_6_window = canvas_correspondant.create_image(145, 170, image = image_clignotant_ring_6, anchor='nw')
    
    

def open_color_to_value():
    '''
    Cette procédure est appelée quand l'utilisateur appuie sur le bouton du mode "Couleur -> valeur"
    Elle met en place la fenêtre avec des paramètres comme la résolution, le titre, ... SEULEMENT si cette fenêtre n'est pas déjà ouverte,
    sinon elle affiche un message d'avertissement à l'utilisateur !
    Puis elle crée une toile ("Canvas") pour la page.
    Ensuite les autres fonctions que l'on vient de voir prennent le relais. 
    '''
    global count_window_open, root_color_to_value
    if count_window_open == 0 :
        root_color_to_value = Toplevel(root)
        root_color_to_value.title("Convertisseur valeurs/couleurs des résistances électriques par Romain MELLAZA")
        root_color_to_value.geometry("1080x720")
        root_color_to_value.minsize(1080, 720)
        root_color_to_value.maxsize(1080, 720)
        canvas_color_to_value = Canvas( root_color_to_value, width = 1080, height = 720)
        canvas_color_to_value.pack(fill = "both", expand = True)
        bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_color_to_value.create_image( 0, 0, image = bg, anchor='nw')
        count_window_open += 1
        tu=canvas_color_to_value.create_text(540, 150, text=' Prenez la resistance dans votre main. \n\n Vous allez devoir répondre à quelques questions \n pour déterminer la valeur de celle-ci ! ', font=("Helvetica", 35), fill="WHITE", justify = CENTER)
        vz=canvas_color_to_value.create_rectangle(canvas_color_to_value.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
        canvas_color_to_value.tag_lower(vz,tu)
        button_validation_2 = Button(root_color_to_value, text="OK ✓", command=lambda *args: open_color_to_value_anneau_1(root_color_to_value), font=("Helvetica", 35), fg='WHITE', bg="#feb58a", height = 2, width = 12)
        canvas_color_to_value.create_window(375, 475, anchor='nw', window=button_validation_2)
        try:
            root_color_to_value.protocol('WM_DELETE_WINDOW', reset)
        except:
            pass
        mainloop()
    else :
        messagebox.showinfo("Erreur","Vous avez déjà ouvert une fenêtre de conversion !")

def open_color_to_value_anneau_1(root_precedent):
    '''
    Fonction complexe qui ouvre la fenêtre pour que l'utilisateur puisse choisir la couleur du premier anneau de sa résistance.
    La fonction admet en paramètre la fenêtre précédente pour qu'elle puisse être détruite.
    '''
    global image_clignotant_ring_1_window, image_clignotant_ring_1, root_color_to_value_anneau_1

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_anneau_1 = Toplevel(root)
    root_color_to_value_anneau_1.title("De quelle couleur est le premier anneau de votre résistance ?")
    root_color_to_value_anneau_1.geometry("1080x720")
    root_color_to_value_anneau_1.minsize(1080, 720)
    root_color_to_value_anneau_1.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_anneau_1 = Canvas( root_color_to_value_anneau_1, width = 1080, height = 720)
    canvas_color_to_value_anneau_1.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_anneau_1.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage de la question pour l'utilisateur :
    tu=canvas_color_to_value_anneau_1.create_text(540, 100, text=' De quelle couleur est le premier \n anneau de votre résistance ? ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    vz=canvas_color_to_value_anneau_1.create_rectangle(canvas_color_to_value_anneau_1.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_anneau_1.tag_lower(vz,tu)

    # Affichage de l'image de la résistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_color_to_value_anneau_1.create_image(145, 170, image = image_resistance_vide, anchor='nw')

    # Affichage de l'image du rond rouge clignotant que je vais passer à la fonction de clignotement que j'ai créé pour qu'elle fasse clignoter l'image :
    image_clignotant_ring_1 = ImageTk.PhotoImage(file = "img/anneau_1/clignotant.png")
    image_clignotant_ring_1_window = canvas_color_to_value_anneau_1.create_image(145, 170, image = image_clignotant_ring_1, anchor='nw')
    etape = 1   # Nous sommes au premier anneau, donc à la première étape !
    clignotement(root_color_to_value_anneau_1, canvas_color_to_value_anneau_1, etape)

    # Je fais apparaître le menu déroulant correspondant et le bouton de validation de la couleur choisie :
    spawn_selecteurs_part2(root_color_to_value_anneau_1, canvas_color_to_value_anneau_1, etape)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre ! 
    try:
        root_color_to_value_anneau_1.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()   # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.

def open_color_to_value_anneau_2(root_precedent):
    '''
    Fonction complexe qui ouvre la fenêtre pour que l'utilisateur puisse choisir la couleur du deuxième anneau de sa résistance.
    La fonction admet en paramètre la fenêtre précédente pour qu'elle puisse être détruite.
    Le programme va afficher l'anneau précédent avec la bonnne couleur choisie par l'utilisateur à la question précédente !
    '''
    global image_clignotant_ring_2_window, image_clignotant_ring_2, root_color_to_value_anneau_2

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_anneau_2 = Toplevel(root)
    root_color_to_value_anneau_2.title("De quelle couleur est le deuxième anneau de votre résistance ?")
    root_color_to_value_anneau_2.geometry("1080x720")
    root_color_to_value_anneau_2.minsize(1080, 720)
    root_color_to_value_anneau_2.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_anneau_2 = Canvas(root_color_to_value_anneau_2, width = 1080, height = 720)
    canvas_color_to_value_anneau_2.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_anneau_2.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage de la question pour l'utilisateur :
    tu=canvas_color_to_value_anneau_2.create_text(540, 100, text=' De quelle couleur est le deuxième \n anneau de votre résistance ? ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    vz=canvas_color_to_value_anneau_2.create_rectangle(canvas_color_to_value_anneau_2.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_anneau_2.tag_lower(vz,tu)

    # Affichage de l'image de la résistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_color_to_value_anneau_2.create_image(145, 170, image = image_resistance_vide, anchor='nw')

    # Dans les structures conditionnelles qui suivent, en gros j'affiche l'image du premier anneau,
    # avec la bonnne couleur choisie par l'utilisateur à la question précédente !
    if chiffre_1 == 1 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/brown.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 2 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/red.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 3 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/orange.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 4 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/yellow.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 5 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/green.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 6 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/blue.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 7 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/purple.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 8 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/grey.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 9 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/white.png")
        canvas_color_to_value_anneau_2.create_image(148, 170, image = image_anneau1, anchor='nw')

    # Affichage de l'image du rond rouge clignotant que je vais passer à la fonction de clignotement que j'ai créé pour qu'elle fasse clignoter l'image :    
    image_clignotant_ring_2 = ImageTk.PhotoImage(file = "img/anneau_2/clignotant.png")
    image_clignotant_ring_2_window = canvas_color_to_value_anneau_2.create_image(145, 170, image = image_clignotant_ring_2, anchor='nw')
    etape = 2   # Nous sommes au second anneau, donc à la deuxième étape !
    clignotement(root_color_to_value_anneau_2, canvas_color_to_value_anneau_2, etape)

    # Je fais apparaître le menu déroulant correspondant et le bouton de validation de la couleur choisie :
    spawn_selecteurs_part2(root_color_to_value_anneau_2, canvas_color_to_value_anneau_2, etape)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre ! 
    try:
        root_color_to_value_anneau_2.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.

def open_color_to_value_anneau_3(root_precedent):
    '''
    Fonction complexe qui ouvre la fenêtre pour que l'utilisateur puisse choisir la couleur du troisième anneau de sa résistance.
    La fonction admet en paramètre la fenêtre précédente pour qu'elle puisse être détruite.
    Le programme va afficher les anneaux précédents avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    '''
    global image_clignotant_ring_3_window, image_clignotant_ring_3, root_color_to_value_anneau_3

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_anneau_3 = Toplevel(root)
    root_color_to_value_anneau_3.title("De quelle couleur est le troisième anneau de votre résistance ?")
    root_color_to_value_anneau_3.geometry("1080x720")
    root_color_to_value_anneau_3.minsize(1080, 720)
    root_color_to_value_anneau_3.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_anneau_3 = Canvas(root_color_to_value_anneau_3, width = 1080, height = 720)
    canvas_color_to_value_anneau_3.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_anneau_3.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage de la question pour l'utilisateur :
    tu=canvas_color_to_value_anneau_3.create_text(540, 100, text=' De quelle couleur est le troisième \n anneau de votre résistance ? ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    vz=canvas_color_to_value_anneau_3.create_rectangle(canvas_color_to_value_anneau_3.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_anneau_3.tag_lower(vz,tu)

    # Affichage de l'image de la résistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_color_to_value_anneau_3.create_image(145, 170, image = image_resistance_vide, anchor='nw')

    # Dans les structures conditionnelles qui suivent, en gros j'affiche l'image des anneaux précédents,
    # avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    if chiffre_1 == 1 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/brown.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 2 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/red.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 3 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/orange.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 4 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/yellow.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 5 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/green.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 6 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/blue.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 7 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/purple.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 8 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/grey.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 9 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/white.png")
        canvas_color_to_value_anneau_3.create_image(148, 170, image = image_anneau1, anchor='nw')
    if chiffre_2 == 0 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/black.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 1 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/brown.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 2 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/red.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 3 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/orange.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 4 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/yellow.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 5 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/green.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 6 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/blue.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 7 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/purple.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 8 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/grey.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 9 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/white.png")
        canvas_color_to_value_anneau_3.create_image(140, 170, image = image_anneau2, anchor='nw')

    # Affichage de l'image du rond rouge clignotant que je vais passer à la fonction de clignotement que j'ai créé pour qu'elle fasse clignoter l'image : 
    image_clignotant_ring_3 = ImageTk.PhotoImage(file = "img/anneau_3/clignotant.png")
    image_clignotant_ring_3_window = canvas_color_to_value_anneau_3.create_image(145, 170, image = image_clignotant_ring_3, anchor='nw')
    etape = 3   # Nous sommes au troisième anneau, donc à la troisième étape.
    clignotement(root_color_to_value_anneau_3, canvas_color_to_value_anneau_3, etape)

    # Je fais apparaître le menu déroulant correspondant et le bouton de validation de la couleur choisie :
    spawn_selecteurs_part2(root_color_to_value_anneau_3, canvas_color_to_value_anneau_3, etape)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre !
    try:
        root_color_to_value_anneau_3.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.

def open_color_to_value_anneau_4(root_precedent):
    '''
    Fonction complexe qui ouvre la fenêtre pour que l'utilisateur puisse choisir la couleur du quatrième anneau de sa résistance.
    La fonction admet en paramètre la fenêtre précédente pour qu'elle puisse être détruite.
    Le programme va afficher les anneaux précédents avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    '''
    global image_clignotant_ring_4_window, image_clignotant_ring_4, root_color_to_value_anneau_4

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_anneau_4 = Toplevel(root)
    root_color_to_value_anneau_4.title("De quelle couleur est le quatrième anneau de votre résistance ?")
    root_color_to_value_anneau_4.geometry("1080x720")
    root_color_to_value_anneau_4.minsize(1080, 720)
    root_color_to_value_anneau_4.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_anneau_4 = Canvas(root_color_to_value_anneau_4, width = 1080, height = 720)
    canvas_color_to_value_anneau_4.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_anneau_4.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage de la question pour l'utilisateur :
    tu=canvas_color_to_value_anneau_4.create_text(540, 100, text=' De quelle couleur est le quatrième \n anneau de votre résistance ? ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    vz=canvas_color_to_value_anneau_4.create_rectangle(canvas_color_to_value_anneau_4.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_anneau_4.tag_lower(vz,tu)

    # Affichage de l'image de la résistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_color_to_value_anneau_4.create_image(145, 170, image = image_resistance_vide, anchor='nw')

    # Dans les structures conditionnelles qui suivent, en gros j'affiche l'image des anneaux précédents,
    # avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    if chiffre_1 == 1 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/brown.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 2 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/red.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 3 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/orange.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 4 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/yellow.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 5 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/green.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 6 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/blue.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 7 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/purple.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 8 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/grey.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 9 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/white.png")
        canvas_color_to_value_anneau_4.create_image(148, 170, image = image_anneau1, anchor='nw')
    if chiffre_2 == 0 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/black.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 1 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/brown.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 2 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/red.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 3 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/orange.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 4 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/yellow.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 5 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/green.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 6 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/blue.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 7 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/purple.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 8 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/grey.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 9 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/white.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau2, anchor='nw')
    if chiffre_3 == 0 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/black.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 1 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/brown.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 2 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/red.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 3 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/orange.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 4 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/yellow.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 5 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/green.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 6 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/blue.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 7 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/purple.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 8 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/grey.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 9 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/white.png")
        canvas_color_to_value_anneau_4.create_image(140, 170, image = image_anneau3, anchor='nw')

    # Affichage de l'image du rond rouge clignotant que je vais passer à la fonction de clignotement que j'ai créé pour qu'elle fasse clignoter l'image :    
    image_clignotant_ring_4 = ImageTk.PhotoImage(file = "img/anneau_4/clignotant.png")
    image_clignotant_ring_4_window = canvas_color_to_value_anneau_4.create_image(145, 170, image = image_clignotant_ring_4, anchor='nw')
    etape = 4   # Nous sommes au quatrième anneau, donc à la quatrième étape.
    clignotement(root_color_to_value_anneau_4, canvas_color_to_value_anneau_4, etape)

    # Je fais apparaître le menu déroulant correspondant et le bouton de validation de la couleur choisie :
    spawn_selecteurs_part2(root_color_to_value_anneau_4, canvas_color_to_value_anneau_4, etape)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre !
    try:
        root_color_to_value_anneau_4.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.

def open_color_to_value_anneau_5(root_precedent):
    '''
    Fonction complexe qui ouvre la fenêtre pour que l'utilisateur puisse choisir la couleur du cinquième anneau de sa résistance.
    La fonction admet en paramètre la fenêtre précédente pour qu'elle puisse être détruite.
    Le programme va afficher les anneaux précédents avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    '''
    global image_clignotant_ring_5_window, image_clignotant_ring_5, root_color_to_value_anneau_5

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_anneau_5 = Toplevel(root)
    root_color_to_value_anneau_5.title("De quelle couleur est le cinquième anneau de votre résistance ?")
    root_color_to_value_anneau_5.geometry("1080x720")
    root_color_to_value_anneau_5.minsize(1080, 720)
    root_color_to_value_anneau_5.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_anneau_5 = Canvas(root_color_to_value_anneau_5, width = 1080, height = 720)
    canvas_color_to_value_anneau_5.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_anneau_5.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage de la question pour l'utilisateur :
    tu=canvas_color_to_value_anneau_5.create_text(540, 100, text=' De quelle couleur est le cinquième \n anneau de votre résistance ? ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    vz=canvas_color_to_value_anneau_5.create_rectangle(canvas_color_to_value_anneau_5.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_anneau_5.tag_lower(vz,tu)

    # Affichage de l'image de la résistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_color_to_value_anneau_5.create_image(145, 170, image = image_resistance_vide, anchor='nw')

    # Dans les structures conditionnelles qui suivent, en gros j'affiche l'image des anneaux précédents,
    # avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    if chiffre_1 == 1 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/brown.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 2 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/red.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 3 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/orange.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 4 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/yellow.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 5 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/green.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 6 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/blue.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 7 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/purple.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 8 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/grey.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 9 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/white.png")
        canvas_color_to_value_anneau_5.create_image(148, 170, image = image_anneau1, anchor='nw')
    if chiffre_2 == 0 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/black.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 1 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/brown.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 2 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/red.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 3 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/orange.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 4 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/yellow.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 5 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/green.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 6 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/blue.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 7 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/purple.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 8 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/grey.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 9 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/white.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau2, anchor='nw')
    if chiffre_3 == 0 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/black.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 1 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/brown.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 2 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/red.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 3 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/orange.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 4 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/yellow.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 5 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/green.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 6 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/blue.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 7 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/purple.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 8 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/grey.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 9 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/white.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau3, anchor='nw')
    if chiffre_4 == 'x1' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/black.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x10' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/brown.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x100' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/red.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x1k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/orange.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x100k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/green.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x1M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/blue.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x10M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/purple.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x100M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/grey.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x1G' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/white.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x0.1' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/gold.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x0.01' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/silver.png")
        canvas_color_to_value_anneau_5.create_image(140, 170, image = image_anneau4, anchor='nw')

    # Affichage de l'image du rond rouge clignotant que je vais passer à la fonction de clignotement que j'ai créé pour qu'elle fasse clignoter l'image :    
    image_clignotant_ring_5 = ImageTk.PhotoImage(file = "img/anneau_5/clignotant.png")
    image_clignotant_ring_5_window = canvas_color_to_value_anneau_5.create_image(145, 170, image = image_clignotant_ring_5, anchor='nw')
    etape = 5   # Nous sommes au cinquième anneau, donc à la cinquième étape.
    clignotement(root_color_to_value_anneau_5, canvas_color_to_value_anneau_5, etape)

    # Je fais apparaître le menu déroulant correspondant et le bouton de validation de la couleur choisie :
    spawn_selecteurs_part2(root_color_to_value_anneau_5, canvas_color_to_value_anneau_5, etape)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre !
    try:
        root_color_to_value_anneau_5.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.

def open_color_to_value_anneau_6(root_precedent):
    '''
    Fonction complexe qui ouvre la fenêtre pour que l'utilisateur puisse choisir la couleur du sixième anneau de sa résistance.
    La fonction admet en paramètre la fenêtre précédente pour qu'elle puisse être détruite.
    Le programme va afficher les anneaux précédents avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    '''
    global image_clignotant_ring_6_window, image_clignotant_ring_6, root_color_to_value_anneau_6

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_anneau_6 = Toplevel(root)
    root_color_to_value_anneau_6.title("De quelle couleur est le sixième anneau de votre résistance ?")
    root_color_to_value_anneau_6.geometry("1080x720")
    root_color_to_value_anneau_6.minsize(1080, 720)
    root_color_to_value_anneau_6.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_anneau_6 = Canvas(root_color_to_value_anneau_6, width = 1080, height = 720)
    canvas_color_to_value_anneau_6.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_anneau_6.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage de la question pour l'utilisateur :
    tu=canvas_color_to_value_anneau_6.create_text(540, 100, text=' De quelle couleur est le sixième \n anneau de votre résistance ? ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    vz=canvas_color_to_value_anneau_6.create_rectangle(canvas_color_to_value_anneau_6.bbox(tu),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_anneau_6.tag_lower(vz,tu)

    # Affichage de l'image de la résistance vide :
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_color_to_value_anneau_6.create_image(145, 170, image = image_resistance_vide, anchor='nw')

    # Dans les structures conditionnelles qui suivent, en gros j'affiche l'image des anneaux précédents,
    # avec les bonnnes couleurs choisies par l'utilisateur aux questions précédentes !
    if chiffre_1 == 1 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/brown.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 2 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/red.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 3 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/orange.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 4 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/yellow.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 5 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/green.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 6 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/blue.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 7 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/purple.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 8 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/grey.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    elif chiffre_1 == 9 :
        image_anneau1 = ImageTk.PhotoImage(file = "img/anneau_1/white.png")
        canvas_color_to_value_anneau_6.create_image(148, 170, image = image_anneau1, anchor='nw')
    if chiffre_2 == 0 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/black.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 1 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/brown.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 2 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/red.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 3 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/orange.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 4 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/yellow.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 5 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/green.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 6 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/blue.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 7 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/purple.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 8 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/grey.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    elif chiffre_2 == 9 :
        image_anneau2 = ImageTk.PhotoImage(file = "img/anneau_2/white.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau2, anchor='nw')
    if chiffre_3 == 0 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/black.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 1 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/brown.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 2 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/red.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 3 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/orange.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 4 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/yellow.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 5 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/green.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 6 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/blue.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 7 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/purple.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 8 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/grey.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    elif chiffre_3 == 9 :
        image_anneau3 = ImageTk.PhotoImage(file = "img/anneau_3/white.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau3, anchor='nw')
    if chiffre_4 == 'x1' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/black.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x10' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/brown.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x100' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/red.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x1k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/orange.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x100k' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/green.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x1M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/blue.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x10M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/purple.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x100M' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/grey.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x1G' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/white.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x0.1' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/gold.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    elif chiffre_4 == 'x0.01' :
        image_anneau4 = ImageTk.PhotoImage(file = "img/anneau_4/silver.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau4, anchor='nw')
    if chiffre_5 == '±1%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/brown.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')
    elif chiffre_5 == '±2%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/red.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')
    elif chiffre_5 == '±0.5%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/green.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')
    elif chiffre_5 == '±0.25%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/blue.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')
    elif chiffre_5 == '±0.10%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/purple.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')
    elif chiffre_5 == '±5%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/gold.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')
    elif chiffre_5 == '±10%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/silver.png")
        canvas_color_to_value_anneau_6.create_image(140, 170, image = image_anneau5, anchor='nw')

    # Affichage de l'image du rond rouge clignotant que je vais passer à la fonction de clignotement que j'ai créé pour qu'elle fasse clignoter l'image :
    image_clignotant_ring_6 = ImageTk.PhotoImage(file = "img/anneau_6/clignotant.png")
    image_clignotant_ring_6_window = canvas_color_to_value_anneau_6.create_image(145, 170, image = image_clignotant_ring_6, anchor='nw')
    etape = 6   # Nous sommes au sixième anneau, donc à la sixième étape !
    clignotement(root_color_to_value_anneau_6, canvas_color_to_value_anneau_6, etape)

    # Je fais apparaître le menu déroulant correspondant et le bouton de validation de la couleur choisie :
    spawn_selecteurs_part2(root_color_to_value_anneau_6, canvas_color_to_value_anneau_6, etape)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre !
    try:
        root_color_to_value_anneau_6.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les images s'affichent en continu et pas seulement une milliseconde.



def open_color_to_value_result(root_precedent):
    '''
    Cette fonction affiche le résultat numérique des différentes couleurs sélectionnées par l'utilisateur.
    '''
    global root_color_to_value_result

    # Le programme détruit la fenêtre précédente :
    root_precedent.destroy()

    # Je défini des paramètres pour la fenêtre (titre, résolution, ...) :
    root_color_to_value_result = Toplevel(root)
    root_color_to_value_result.title("Voici la valeur de votre résistance !")
    root_color_to_value_result.geometry("1080x720")
    root_color_to_value_result.minsize(1080, 720)
    root_color_to_value_result.maxsize(1080, 720)

    # Création de la toile correspondante et affichage de l'image de fond dessus :
    canvas_color_to_value_result = Canvas(root_color_to_value_result, width = 1080, height = 720)
    canvas_color_to_value_result.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_color_to_value_result.create_image( 0, 0, image = bg, anchor='nw')

    # Affichage du titre sur la page :
    fin=canvas_color_to_value_result.create_text(540, 100, text=' Voici la valeur \n de votre résistance électrique : ', font=("Helvetica", 45), fill="WHITE", justify = CENTER)
    ito=canvas_color_to_value_result.create_rectangle(canvas_color_to_value_result.bbox(fin),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_result.tag_lower(ito,fin)

    # Structures conditionnelles pour afficher lke bon nombre de valeurs en fonction du nombre d'anneaux fournit par l'utilisateur :
    if chiffre_3 != None and chiffre_6 != None :    # Si il s'agit d'une résistance 6 bandes.
        resultat = chiffre_1,chiffre_2,chiffre_3,chiffre_4, 'Ω',chiffre_5,chiffre_6
    
    elif chiffre_3 == None and chiffre_6 != None :  # Si il s'agit d'une résistance 5 bandes, qui ne possède pas de troisième chiffre significatif.
        resultat = chiffre_1,chiffre_2,chiffre_4, 'Ω',chiffre_5,chiffre_6

    
    elif chiffre_3 != None and chiffre_6 == None :  # Si il s'agit d'une résistance 5 bandes, qui ne possède pas de coefficient de température.
        resultat = chiffre_1,chiffre_2,chiffre_3,chiffre_4, 'Ω',chiffre_5
    
    elif chiffre_3 == None and chiffre_6 == None :  # Si il s'agit d'une résistance 4 bandes.
        resultat = chiffre_1,chiffre_2,chiffre_4, 'Ω',chiffre_5
    
    # Affichage du résultat :
    abc=canvas_color_to_value_result.create_text(540, 450, text=resultat, font=("Helvetica", 50), fill="WHITE", justify = CENTER)
    gui=canvas_color_to_value_result.create_rectangle(canvas_color_to_value_result.bbox(abc),fill="#feb58a", width = 1, outline = 'BLACK')
    canvas_color_to_value_result.tag_lower(gui,abc)

    # Ces lignes de codes permettent au programme d'actionner la fonction de réinitialisation des variables si il reçoit l'information que l'utilisateur essaie de fermer la fenêtre de conversion :
    # Cela permet donc à l'utilisateur de réaliser autant de conversion qu'il souhaite même si il ferme la fenêtre !
    try:
        root_color_to_value_result.protocol('WM_DELETE_WINDOW', reset)
    except:
        pass

    mainloop()  # Je rafraîchis continuellement la page pour que les textes s'affichent en continu et pas seulement une milliseconde.



##############################################################################################################################################################################################################
#                                                                            INTERRACTIONS POSSIBLES DANS L'ACCUEIL                                                                                          #
#                                                                                                                                                                                                            #


# Définition du bouton pour sélectionner le mode de conversion de valeur à couleur :
button_value_to_color = Button(root, text="Valeur ➔ Couleur", command=open_value_to_color, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_value_to_color_window = canvas_accueil.create_window(30, 425, anchor='nw', window=button_value_to_color)

# Définition du bouton pour sélectionner le mode de conversion de couleur à valeur :
button_color_to_value = Button(root, text="Couleur ➔ Valeur", command=open_color_to_value, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_color_to_value_window = canvas_accueil.create_window(560, 425, anchor='nw', window=button_color_to_value)

def reset():
    '''
    Cette procédure permet de réinitialiser le compteur de fenêtre ouverte si l'utilisatuer en ferme une.
    Le programme la ferme par la suite en vérifiant qu'il n'y a pas de "sous-fenêtre" à fermer aussi.
    '''
    global count_window_open
    count_window_open = 0
    try :
        root_value_to_color.destroy()
    except :
        pass
    try :
        root_color_to_value.destroy()
    except :
        pass
    try :
        root_color_to_value_anneau_1.destroy()
    except :
        pass
    try :
        root_color_to_value_anneau_2.destroy()
    except :
        pass
    try :
        root_color_to_value_anneau_3.destroy()
    except :
        pass
    try :
        root_color_to_value_anneau_4.destroy()
    except :
        pass
    try :
        root_color_to_value_anneau_5.destroy()
    except :
        pass
    try :
        root_color_to_value_anneau_6.destroy()
    except :
        pass
    try :
        root_color_to_value_result.destroy()
    except :
        pass

def msg_remerciement():
    '''
    Cette procédure affiche un message de remerciement lorsque l'utilisateur ferme la fenêtre principale.
    Puis elle met fin au fonctionnement de celle-ci.
    '''
    messagebox.showinfo('MERCI !',"Merci d'avoir utilisé mon logiciel ! :)")
    root.destroy()

# Ces lignes de codes permettent au programme d'actionner la fonction de remerciement si il reçoit l'information que l'utilisateur essaie de fermer le logiciel :
try:
    root.protocol('WM_DELETE_WINDOW', msg_remerciement)
except:
    pass

# Je rafraîchis continuellement mon application via cette commande :
root.mainloop()