import tkinter as tk
from clase import Contador
import tkinter.messagebox as msg
import ttkbootstrap as btp
from tkinter import ttk
from tkinter import Toplevel, ttk

principal = btp.Window(themename="lumen")
principal.geometry('400x400')
principal.title("Inicio de sesión")
principal.config(bg="light blue")

matriz_con_labels = [[0,0,0],[0,0,0],[0,0,0]]

def abrirVentana():
    ventana = Toplevel()
    ventana.config(width=300, height=300)
    ventana.resizable(0, 0)
    ventana.title("TATETI - Jugador 1")
    
    for i in range(3): 
        for n in range(3):
            matriz_con_labels[i][n] = tk.Label(ventana, text=".",)
            matriz_con_labels[i][n].config(border = 0, bg = "light blue", padx=50, pady=50, borderwidth=1, relief=tk.SOLID)
            matriz_con_labels[i][n].grid(row=i, column=n)
            matriz_con_labels[i][n].bind("<Button>", lambda event, obj=[i,n,ventana]: eventos(event, obj))









#label

lblTitulo = ttk.Label(principal, text="Bienvenido al Ta Te Ti", bootstyle=(
    "PRIMARY", "INVERSE-PRIMARY"), font=("Helvetica", 18)).place(x=80, y=30)
#fondo
imagenTaTeTi = tk.PhotoImage(file="D:\Desktop\Tateti\Tictac.png")
fondo = tk.Label(principal, image=imagenTaTeTi).place(x=100, y=100)

button=ttk.Button(principal,text='¡COMENZAR A JUGAR!',command=abrirVentana, bootstyle = ("PRIMARY", "OUTLINE")).place(x=120, y=320)



juego_global = [["*", "*", "*"],["*", "*", "*"],["*", "*", "*"]]

juego_finalizado = False; jugador_1 = "turno"; jugador_2 = "espera"; contador = Contador()

def quien_gano(lista, simbolo):
    ganador = False
    if(lista[0][0] == simbolo and lista[0][1] == simbolo and lista[0][2] == simbolo): 
        ganador = True
    if(lista[1][0] == simbolo and lista[1][1] == simbolo and lista[1][2] == simbolo):
        ganador = True
    if(lista[2][0] == simbolo and lista[2][1] == simbolo and lista[2][2] == simbolo):
        ganador = True
    if(lista[0][0] == simbolo and lista[1][0] == simbolo and lista[2][0] == simbolo):
        ganador = True
    if(lista[0][1] == simbolo and lista[1][1] == simbolo and lista[2][1] == simbolo):
        ganador = True
    if(lista[0][2] == simbolo and lista[1][2] == simbolo and lista[2][2] == simbolo):
        ganador = True
    if(lista[0][0] == simbolo and lista[1][1] == simbolo and lista[2][2] == simbolo):
        ganador = True
    if(lista[0][2] == simbolo and lista[1][1] == simbolo and lista[2][0] == simbolo):
        ganador = True

    return ganador


def eventos(event, obj):
    global contador
    global jugador_1
    global jugador_2
    if (jugador_1 == "turno"): 
        juego_global[obj[0]][obj[1]] = "X"
        matriz_con_labels[obj[0]][obj[1]].config(text="X")
        obj[2].title("TATETI - Jugador 1")
        jugador_1 = "espera"
        jugador_2 = "turno"
    else: 
        juego_global[obj[0]][obj[1]] = "O"
        matriz_con_labels[obj[0]][obj[1]].config(text="O")
        obj[2].title("TATETI - Jugador 2")
        jugador_1 = "turno"
        jugador_2 = "espera"

    if (quien_gano(juego_global, "X")):
        msg.showinfo("Ganador","Gano jugador X")
        juego_finalizado = True
    if (quien_gano(juego_global, "O")): 
        msg.showinfo("Ganador","Gano jugador O")
        juego_finalizado = True
    contador.set_contador()
    if (contador.get_contador() == 9): 
        msg.showinfo("Juego empatado","Juego empatado")
    


    #print(juego_global[0])
    #print(juego_global[1])
    #print(juego_global[2])
    #print("")



#fin interfaz gráfica
principal.mainloop()
