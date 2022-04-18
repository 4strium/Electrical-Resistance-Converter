

from tkinter import *
from tkinter import messagebox
from PIL import *

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

button_value_to_color = Button(root, text="Valeur ➔ Couleur", command=None, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_value_to_color_window = canvas_accueil.create_window(30, 425, anchor='nw', window=button_value_to_color)

button_color_to_value = Button(root, text="Couleur ➔ Valeur", command=None, font=("Helvetica", 35), fg='white', bg="#feb58a", height = 2, width = 18)
button_color_to_value_window = canvas_accueil.create_window(560, 425, anchor='nw', window=button_color_to_value)









root.mainloop()