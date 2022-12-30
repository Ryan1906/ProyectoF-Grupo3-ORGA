import tkinter as tk
import tkinter
from tkinter import messagebox

import time
import serial

serial = serial.Serial(port='COM6', baudrate=9600, timeout=1)


global PoolState
PoolState = 0

global luces
luces = 0
global luces2
luces2 = 0
global luces3
luces3 = 0
global luces4
luces4 = 0



ventana = tkinter.Tk()
ventana.geometry("500x400")
ventana["bg"]= '#E73E1A'
ventana.title("PANEL DE CONTROL")


def VentanaLuces():

    ventana = tkinter.Tk()
    ventana.geometry("900x300")
    ventana["bg"]= '#E73E1A'
    ventana.title("LUCES")

    

   

    def Luz1():
    
        global luces
        global data
        if luces == 0:
           

            LucesCuadro["bg"] = "#E1FD2D"

            luces =1
            serial.write(b'C')
            
            print(luces)

        elif luces == 1:

            

            LucesCuadro["bg"] = "#808080"
            luces=0
            serial.write(b'D')
            serial.write(b' ')
            print(luces)

    
    def Luz2():
    
        global luces2
        global data
        if luces2 == 0:
           

            LucesCuadro2["bg"] = "#E1FD2D"
            
            serial.write(b'E')
            luces2 =1

            print(luces2)

        elif luces2 == 1:

            
            serial.write(b'F')
            serial.write(b' ')
            LucesCuadro2["bg"] = "#808080"
            luces2=0
            print(luces2)

    def Luz3():
    
        global luces3
        global data
        if luces3 == 0:
           

            LucesCuadro3["bg"] = "#E1FD2D"
            serial.write(b'G')
            
            luces3 =1

            print(luces3)

        elif luces3 == 1:

            

            LucesCuadro3["bg"] = "#808080"
            luces3=0
            serial.write(b'H')
            serial.write(b' ')
            print(luces3)
    
    def Luz4():
    
        global luces4
        global data
        if luces4 == 0:
           

            LucesCuadro4["bg"] = "#E1FD2D"

            luces4 =1
           
            serial.write(b'I')
            print(luces4)

        elif luces4 == 1:

            

            LucesCuadro4["bg"] = "#808080"
            luces4=0
            serial.write(b'J')
            serial.write(b' ')
            print(luces4)

        



    
    LucesCuadro  = tkinter.Label(ventana,fg = "Black" ,  height=2, width= 10, font= ("Arial", 15))
    LucesCuadro["bg"] = "#5D5D5D"

    LucesCuadro2  = tkinter.Label(ventana,fg = "Black" ,  height=2, width= 10, font= ("Arial", 15))
    LucesCuadro2["bg"] = "#5D5D5D"

    LucesCuadro3  = tkinter.Label(ventana,fg = "Black" ,  height=2, width= 10, font= ("Arial", 15))
    LucesCuadro3["bg"] = "#5D5D5D"

    LucesCuadro4  = tkinter.Label(ventana,fg = "Black" ,  height=2, width= 10, font= ("Arial", 15))
    LucesCuadro4["bg"] = "#5D5D5D"

    LucesCuadro.place(x = 500,y=90)

    LucesCuadro2.place(x = 650,y=90)

    LucesCuadro3.place(x = 500,y=170)

    LucesCuadro4.place(x = 650,y=170)

    TextoTituloL  = tkinter.Label(ventana,text="CONTROL DE LUCES",fg = "Black" ,  height=2, width= 30, font= ("Arial", 15))
    TextoTituloL["bg"] = "#F7D3CC"

    TextoTituloL.place(x = 80,y=10)

    BTN_Principal = tkinter.Button(ventana, text = "Dormitorio Principal", fg= "Black", height= 2, width= 20, command= Luz1)
    BTN_Garage = tkinter.Button(ventana, text = "Garage", fg= "Black", height= 2, width= 20, command= Luz3)
    BTN_Secundario = tkinter.Button(ventana, text = "Dormitorio 2", fg= "Black", height= 2, width= 20, command =Luz2)
    BTN_Terciario = tkinter.Button(ventana, text = "Dormitorio 3", fg= "Black", height= 2, width= 20,  command =Luz4)

    BTN_Secundario.place(x=270, y=100)
    BTN_Terciario.place(x=270, y=160)
    BTN_Principal.place(x=100,y=100)
    BTN_Garage.place(x=100,y=160)

def VentanaPiscina():
    ventana = tkinter.Tk()
    ventana.geometry("500x400")
    ventana["bg"]= '#E73E1A'
    ventana.title("PISCINA")


    def Llenar():
    
        global PoolState
        
        if PoolState == 0:
           

            PiscinaCuadro["bg"] = "#2D9BFD"

            PoolState =1
            serial.write(b'A')
            print(PoolState)

        elif PoolState == 1:

            

            messagebox.showinfo(message="La Piscina ya está llena", title="Título")
            
            
            print(PoolState)

    def Vaciar():
    
        global PoolState
        
        if PoolState == 1:
           

            PiscinaCuadro["bg"] = "#757575"

            PoolState =0
            serial.write(b'B')
            print(PoolState)

        elif PoolState == 0:

            

            messagebox.showinfo(message="La Piscina ya está Vacía", title="Título")
            
            serial.write(b'J')
            print(PoolState)
            



    PiscinaCuadro  = tkinter.Label(ventana,fg = "Black" ,  height=8, width= 20, font= ("Arial", 15))
    PiscinaCuadro["bg"] = "#5D5D5D"

    PiscinaCuadro.place(x = 220,y=100)

    TextoTituloL  = tkinter.Label(ventana,text="CONTROL DE PISCINA",fg = "Black" ,  height=2, width= 30, font= ("Arial", 15))
    TextoTituloL["bg"] = "#F7D3CC"

    TextoTituloL.place(x = 80,y=10)
    BTN_Llenar = tkinter.Button(ventana, text = "LLENAR PISCINA", fg= "Black", height= 2, width= 20, command=Llenar)
    BTN_Vaciar = tkinter.Button(ventana, text = "VACIAR PISCINA", fg= "Black", height= 2, width= 20, command=Vaciar)

    BTN_Llenar.place(x=50, y=100)
    BTN_Vaciar.place(x=50, y=160)





TextoTitulo  = tkinter.Label(ventana,text="PANEL DE CONTROL",fg = "Black" ,  height=2, width= 30, font= ("Arial", 15))
TextoTitulo["bg"] = "#F7D3CC"

TextoTitulo.place(x = 80,y=10)





BTN_Luces = tkinter.Button(ventana, text = "LUCES", fg= "Black", height= 2, width= 20, command= VentanaLuces)
BTN_Piscina = tkinter.Button(ventana, text = "PISCINA", fg= "Black", height= 2, width= 20, command= VentanaPiscina)
BTN_Luces.place(x=170,y=150)
BTN_Piscina.place(x=170,y=220)




ventana.mainloop()