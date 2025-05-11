import requests
import json
import openpyxl
import matplotlib.pyplot as plt
import statistics

token="53b9daf9-5d6d-b34f-ddcd-3f2500d6faab"
url = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000001,1002000058,1002000061,1002000067,1002000070,1002000073,1002000076,1002000079,1002000082,1002000085/es/0700/true/BISE/2.0/{token}?type=json"

def extraer_datos(lista):
	peticion = requests.get(url)
	print(peticion.status_code) 
	datos=peticion.json()
	print("{:<15} {:<15} {:<15}".format("Indicador","Periodo", "Total de personas" ))
	valores=[]
	for dato in datos["Series"]:
		lista.append((dato["INDICADOR"],dato["OBSERVATIONS"][0]["TIME_PERIOD"],float(dato["OBSERVATIONS"][0]["OBS_VALUE"])))
		print("{:<15} {:<15} {:<15}".format(dato["INDICADOR"],dato["OBSERVATIONS"][0]["TIME_PERIOD"],float(dato["OBSERVATIONS"][0]["OBS_VALUE"])))
		valores.append(float(dato["OBSERVATIONS"][0]["OBS_VALUE"]))
	print("\nAnálisis estadístico de los datos:")
	print(f"Valores analizados:")
	media=statistics.mean(valores)
	mediana=statistics.median(valores)
	try:
		moda=statistics.mode(valores)
	except statistics.StatisticsError:
		moda="No hay una sola moda" 
	varianza=statistics.variance(valores)
	desviacion=statistics.stdev(valores)
 
	print(f"Media: {media}")
	print(f"Mediana: {mediana}")
	print(f"Moda: {moda}")
	print(f"Varianza: {varianza}")
	print(f"Desviación estándar: {desviacion}")
	return 

def guardar_excel(lista):
	nombres = [
	("Descripcion",""),
  	("Población de 15 a 19 años",""),
   	("Población de 0 a 4 años",""),
   	("Población de 10 a 14 años",""),
    	("Población Total",""),
    	("Población de 20 a 24 años",""),
    	("Población de 25 a 29 años",""),
    	("Población de 30 a 34 años",""),
    	("Población de 35 a 39 años",""),
   	("Población de 40 a 44 años",""),
    	("Población de 45 a 49 años",""),
	]
	excel_guardar=openpyxl.Workbook()
	sheet=excel_guardar.active
	for index, pos in enumerate(lista):
		sheet[f"A{index+1}"]=pos[0]
		sheet[f"C{index+1}"]=pos[1]
		sheet[f"D{index+1}"]=pos[2]
	for index, pos in enumerate(nombres):
		sheet[f"B{index+1}"]=pos[0]
	excel_guardar.save("datos.xlsx")
	print("\nSe guardaron los datos con exito")
	return

def ver_grafica():
	response = requests.get(url)
	info = response.json()
	nombres = [
   	"Población de 15 a 19 años",
   	"Población de 0 a 4 años",
   	"Población de 10 a 14 años",
    	"Población Total",
    	"Población de 20 a 24 años",
    	"Población de 25 a 29 años",
    	"Población de 30 a 34 años",
    	"Población de 35 a 39 años",
   	 "Población de 40 a 44 años",
    	"Población de 45 a 49 años",
	]
	valores = []
	for i in info.get("Series", []):
    		value = i.get("OBSERVATIONS", [{}])[0].get("OBS_VALUE", None)
    		if value is not None:
        		valores.append(float(value))
	plt.bar(nombres, valores)
	plt.xticks(rotation=45, ha="right")
	plt.tight_layout()
	plt.show()
	return