'''
Ejercicio 27 
En una empresa se almacenaron los sueldos de 10 personas. 
Desarrollar las siguientes funciones y llamarlas desde el bloque principal: 
1) Carga de los sueldos en una lista. 
2) Impresión de todos los sueldos. 
3) Cuántos tienen un sueldo superior a $4000. 
4) Retornar el promedio de los sueldos. 
5) Mostrar todos los sueldos que están por debajo del promedio.
'''

def cargaSueldos():
    sueldos = []
    for i in range (10):
        sueldos.append(int(input('Ingrese el sueldo: ')))
    return sueldos

def imprimirSueldos(sueldos):
    for i in range (len(sueldos)):
        print(sueldos[i])

def sueldosSuperior(sueldos):
    contador = 0
    for i in range (len(sueldos)):
        if sueldos[i] > 4000:
            contador += 1
    return contador

def promedioSueldos(sueldos):
    promedio = sum(sueldos) / len(sueldos)
    return promedio

def sueldosDebajo(sueldos):
    for i in range (len(sueldos)):
        if sueldos[i] < promedioSueldos(sueldos):
            print(sueldos[i])
            
sueldos = cargaSueldos()
print('Los sueldos son: ')
imprimirSueldos(sueldos)
print(f'Los sueldos superiores a $4000 son: {sueldosSuperior(sueldos)}')
print(f'El promedio de los sueldos es: {promedioSueldos(sueldos)}')
print('Los sueldos por debajo del promedio son: ')
sueldosDebajo(sueldos)


