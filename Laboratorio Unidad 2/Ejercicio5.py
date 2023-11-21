"""
Ejercicio 5 
Millas y kilómetros son unidades de longitud o distancia. 
Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, realiza un programa que devuelva la siguiente salida: 
Convierte de Millas a kilómetros. Convierte de Kilómetros a millas. Ayuda: utiliza la funcion round para redondear a 2 digitos. 
"""
proporcion = 1.61

millas = float(input("Ingrese la cantidad de millas a convertir a kilometros: "))
kilometros = float(input("Ingrese la cantidad de kilometros a convertir a millas: "))

print(millas," millas son ",round(millas * proporcion, 2)," kilometros\n",kilometros,"kilometros son ",round(kilometros / proporcion, 2)," millas")



