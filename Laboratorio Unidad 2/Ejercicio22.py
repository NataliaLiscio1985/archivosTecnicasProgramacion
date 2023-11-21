"""
Ejercicio 22 
Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y empatados, 
por ABC club en el torneo apertura, se debe de mostrar su puntaje total, teniendo en cuenta que por cada partido ganado 
obtendrá 3 puntos, empatado 1 punto y perdido 0 puntos. 
"""

ganados = int(input("Ingrese la cantidad de partidos ganados: "))
puntganados = ganados * 3
empatados = int(input("Ingrese la cantidad de partidos empatados: "))
perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
puntaje = puntganados + empatados
print("*****DETALLE DE PUNTOS*****")
print("Partidos ganados:   ",ganados, "con ",puntganados," puntos")
print("Partidos empatados: ",empatados,"con ", empatados," puntos")
print("Partidos perdidos:  ",perdidos,"con  0  puntos")
print("Puntaje total:             ",puntaje,"puntos")

