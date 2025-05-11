import PIA_modulo
import requests
import json
import openpyxl
import matplotlib.pyplot as plt

def main():
	lista=[
			("Indicador", "Periodo", "Total de personas")
		]
	pase=0
	print("1.-Extraer datos")
	print("2.-Guardarlos en excel")
	print("3.-Grafica")
	print("4.-Salir")
	opcion=int(input("Seleccione una opcion: "))
	while opcion!=4:
		if opcion==1:
			pase=1
			PIA_modulo.extraer_datos(lista)
		if opcion==2:
			if pase==0:
				print("\nPrimero extraiga los datos para guardar en excel")
			else:
				PIA_modulo.guardar_excel(lista)
		if opcion==3:
			if pase==0:
				print("\nPrimero extraiga los datos para mostrar la grafica")
			else:
				PIA_modulo.ver_grafica()

		print("\n1.-Extraer datos")
		print("2.-Guardarlos en excel")
		print("3.-Grafica")
		print("4.-Salir")
		opcion=int(input("Seleccione una opcion: "))

main()