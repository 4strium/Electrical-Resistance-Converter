

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

root = Tk()

root.title("Convertisseur valeurs/couleurs des résistances électriques par Romain MELLAZA")
root.geometry("1080x720")
root.minsize(1080, 720)
root.maxsize(1080, 720)
root.iconbitmap(default='icon\LOGO_resistance.ico')


bg = PhotoImage(file = "img\Background_IMAGE.png")
canvas_accueil = Canvas( root, width = 1080, height = 720)
canvas_accueil.pack(fill = "both", expand = True)
canvas_accueil.create_image( 0, 0, image = bg, anchor = "nw")


i=canvas_accueil.create_text(540.45, 137, text='Bienvenue dans le convertisseur\nde résistance électrique !', font=("Helvetica", 42), fill="white", justify = CENTER)
r=canvas_accueil.create_rectangle(canvas_accueil.bbox(i),fill="#feb58a", width = 1)                                                            
canvas_accueil.tag_lower(r,i)


k=canvas_accueil.create_text(540.45, 310, text='Quelle conversion voulez-vous réaliser ?', font=("Helvetica", 35), fill="white")
l=canvas_accueil.create_rectangle(canvas_accueil.bbox(k),fill="#feb58a", width = 1)
canvas_accueil.tag_lower(l,k)


valeur_anneau_1 = [
    # 0 impossible
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

valeur_anneau_2 = [
    "0",
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

valeur_anneau_3 = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "Aucun" # Possibilité de ne pas avoir de 3ème chiffre siginicatif
]

valeur_multipli = [
    "x1",
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

valeur_tolerance = [
    "±10%",
    "±5%",
    "±2%",
    "±1%",
    "±0.5%",
    "±0.25%",
    "±0.10%"
]

valeur_temperature = [
    "250ppm/K",
    "100ppm/K",
    "50ppm/K",
    "25ppm/K",
    "20ppm/K",
    "15ppm/K",
    "10ppm/K",
    "5ppm/K",
    "1ppm/K",
    "Aucun"
]


def image_converter(root_correspondant, canvas_correspondant, ring1, ring2, ring3, ring4, ring5, ring6):
    image_resistance_vide = ImageTk.PhotoImage(file = "img/blank_resistance.png")
    canvas_correspondant.create_image( 50, 170, image = image_resistance_vide, anchor='nw')
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
    elif ring5.get() == '±0.1%' :
        image_anneau5 = ImageTk.PhotoImage(file = "img/anneau_5/purple.png")
        canvas_correspondant.create_image( 50, 170, image = image_anneau5, anchor='nw')
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
    
    mainloop()


def spawn_selecteurs(root_correspondant, canvas_correspondant):
    global valeur_anneau_1, valeur_anneau_2, valeur_anneau_3, valeur_multipli, valeur_tolerance, valeur_temperature
    anneau1 = StringVar()
    anneau1.set(valeur_anneau_1[0])
    drop_chiffre_1 = OptionMenu(root_correspondant, anneau1, *valeur_anneau_1)
    drop_chiffre_1.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_1["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(50, 125, anchor='nw', window=drop_chiffre_1)
    a=canvas_correspondant.create_text(138, 85, text='1er\nchiffre significatif :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    b=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(a),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(b,a)
    anneau2 = StringVar()
    anneau2.set(valeur_anneau_2[0])
    drop_chiffre_2 = OptionMenu(root_correspondant, anneau2, *valeur_anneau_2)
    drop_chiffre_2.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_2["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(250, 125, anchor='nw', window=drop_chiffre_2)
    c=canvas_correspondant.create_text(338, 85, text='2ème\nchiffre significatif :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    d=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(c),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(d,c)
    anneau3 = StringVar()
    anneau3.set(valeur_anneau_3[10])
    drop_chiffre_3 = OptionMenu(root_correspondant, anneau3, *valeur_anneau_3)
    drop_chiffre_3.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_3["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(450, 125, anchor='nw', window=drop_chiffre_3)
    e=canvas_correspondant.create_text(538, 85, text='3ème\nchiffre significatif :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    f=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(e),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(f,e)
    anneau_multipli = StringVar()
    anneau_multipli.set(valeur_multipli[0])
    drop_chiffre_multipli = OptionMenu(root_correspondant, anneau_multipli, *valeur_multipli)
    drop_chiffre_multipli.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_multipli["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(650, 125, anchor='nw', window=drop_chiffre_multipli)
    g=canvas_correspondant.create_text(738, 85, text='Multiplicateur :\n', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    h=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(g),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(h,g)
    anneau_tolerance = StringVar()
    anneau_tolerance.set(valeur_tolerance[0])
    drop_chiffre_tolerance = OptionMenu(root_correspondant, anneau_tolerance, *valeur_tolerance)
    drop_chiffre_tolerance.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_tolerance["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(850, 125, anchor='nw', window=drop_chiffre_tolerance)
    o=canvas_correspondant.create_text(938, 85, text='Tolérance :\n', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    p=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(o),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(p,o)
    anneau_temperature = StringVar()
    anneau_temperature.set(valeur_temperature[9])
    drop_chiffre_temperature = OptionMenu(root_correspondant, anneau_temperature, *valeur_temperature)
    drop_chiffre_temperature.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_temperature["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(850, 650, anchor='nw', window=drop_chiffre_temperature)
    t=canvas_correspondant.create_text(938, 610, text='Coefficient\ntempérature :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    u=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(t),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(u,t)
    button_validation = Button(root_correspondant, text="Valider ✓", command=lambda *args: image_converter(root_correspondant, canvas_correspondant, anneau1, anneau2, anneau3, anneau_multipli, anneau_tolerance, anneau_temperature), font=("Helvetica", 18), fg='BLACK', bg="#feb58a", height = 2, width = 12)
    canvas_correspondant.create_window(870, 380, anchor='nw', window=button_validation)
    image_converter(root_correspondant, canvas_correspondant, anneau1, anneau2, anneau3, anneau_multipli, anneau_tolerance, anneau_temperature)



def open_value_to_color():
    root_value_to_color = Toplevel(root)
    root_value_to_color.title("Convertisseur valeurs/couleurs des résistances électriques par Romain MELLAZA")
    root_value_to_color.geometry("1080x720")
    root_value_to_color.minsize(1080, 720)
    root_value_to_color.maxsize(1080, 720)
    canvas_value_to_color = Canvas( root_value_to_color, width = 1080, height = 720)
    canvas_value_to_color.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_value_to_color.create_image( 0, 0, image = bg, anchor='nw')
    spawn_selecteurs(root_value_to_color, canvas_value_to_color)

button_value_to_color = Button(root, text="Valeur ➔ Couleur", command=open_value_to_color, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_value_to_color_window = canvas_accueil.create_window(30, 425, anchor='nw', window=button_value_to_color)

button_color_to_value = Button(root, text="Couleur ➔ Valeur", command=open_value_to_color, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_color_to_value_window = canvas_accueil.create_window(560, 425, anchor='nw', window=button_color_to_value)







root.mainloop()