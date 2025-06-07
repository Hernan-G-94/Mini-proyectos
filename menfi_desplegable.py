import tkinter as tk
ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label=
                        'Principal', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label='Opciones', menu=submenu)
submenu.add_command(label='Opcion 1')
submenu.add_command(label='Opcion 2')
ventana.mainloop()