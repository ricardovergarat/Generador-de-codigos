from tkinter import *
import os

#UTF-8

def La_GUI():
    ventana = Tk()
    ventana.mainloop()

def determinar_la_ruta_actual():
	ruta = os.getcwd()
	return ruta

def determinar_nombre_de_usuario(ubicacion):
	ubicacion = ubicacion.split("\\")
	tamaño = len(ubicacion)
	if tamaño >= 3:
		return ubicacion[2]
	else:
		return False

def preguntar_si_iniciamos_el_programa(nombre):
	if nombre == False:
		print("No se pudo recuperar el nombre de usuario")
		print("Puede dejar el programa en documentos,musica,videos o el escritorio para recuperar el nombre de usuario")
		return False
	else:
		return True

def decidir_iniciar(activacion):
	if activacion == True:
		pass
	else:
		print("El programa no se ejecuto")

#def ruta_de_salida():
#	salida = "C:\Users\ricardo\Desktop"
#	return 0


_name_ = "_main_"
if _name_ == "_main_":
	ubicacion = determinar_la_ruta_actual()
	usario = determinar_nombre_de_usuario(ubicacion)
	activacion = preguntar_si_iniciamos_el_programa(usario)
	decidir_iniciar(activacion)

    #La_GUI()
