

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
    "±4%",
    "±3%",
    "±2%",
    "±1%",
    "±0.5%",
    "±0.25%",
    "±0.10%",
    "±0.05%"
]

valeur_temperature = [
    "200ppm",
    "100ppm",
    "50ppm",
    "25ppm",
    "15ppm",
    "10ppm",
    "5ppm",
    "Aucun"
]


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
    anneau_temperature.set(valeur_temperature[7])
    drop_chiffre_temperature = OptionMenu(root_correspondant, anneau_temperature, *valeur_temperature)
    drop_chiffre_temperature.config(width = 10, font=("Helvetica", 18), fg ='black', bg="#feb58a", activebackground="#feb58a")
    drop_chiffre_temperature["menu"].config(font=("Helvetica", 12), fg ='black', bg="#feb58a", activebackground="#feb58a")
    canvas_correspondant.create_window(850, 650, anchor='nw', window=drop_chiffre_temperature)
    t=canvas_correspondant.create_text(938, 610, text='Coefficient\ntempérature :', font=("Helvetica", 16), fill="BLACK", justify = CENTER)
    u=canvas_correspondant.create_rectangle(canvas_correspondant.bbox(t),fill="#feb58a", width = 1, outline = 'white')
    canvas_correspondant.tag_lower(u,t)




def open_value_to_color():
    root_value_to_color = Toplevel(root)
    root_value_to_color.title("Conversion d'une valeur au code couleur d'une résistance électrique")
    root_value_to_color.geometry("1080x720")
    root_value_to_color.minsize(1080, 720)
    root_value_to_color.maxsize(1080, 720)
    canvas_value_to_color = Canvas( root_value_to_color, width = 1080, height = 720)
    canvas_value_to_color.pack(fill = "both", expand = True)
    bg = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_value_to_color.create_image( 0, 0, image = bg, anchor='nw')
    spawn_selecteurs(root_value_to_color, canvas_value_to_color)
    mainloop()

button_value_to_color = Button(root, text="Valeur ➔ Couleur", command=open_value_to_color, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_value_to_color_window = canvas_accueil.create_window(30, 425, anchor='nw', window=button_value_to_color)

button_color_to_value = Button(root, text="Couleur ➔ Valeur", command=open_value_to_color, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_color_to_value_window = canvas_accueil.create_window(560, 425, anchor='nw', window=button_color_to_value)







root.mainloop()