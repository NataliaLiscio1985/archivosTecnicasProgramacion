'''
Ejercicio 7 
 
El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por 
ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros. 
En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de 
combustible. 
Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa. 

Las funciones: 
se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente; 
toman un argumento (el valor correspondiente a sus nombres) 
Complementa el código en el editor y ejecuta tu código y verifica si tu salida es la misma que la 
nuestra. 
 
Información para ayudarte: 
1 milla = 1609.344 metros. 
1 galón = 3.785411784 litros. 
'''

def liters_100km_to_miles_gallon(litros):
    galon = litros / 3.785411784
    millas = 100000 / 1609.344
    return millas / galon

def miles_gallon_to_liters_100km(millas):
    kilometros = millas * 1609.344 / 100000
    litros = 3.785411784 
    return litros / kilometros

print(liters_100km_to_miles_gallon(3.9)) 
print(liters_100km_to_miles_gallon(7.5)) 
print(liters_100km_to_miles_gallon(10.)) 
print(miles_gallon_to_liters_100km(60.3)) 
print(miles_gallon_to_liters_100km(31.4)) 
print(miles_gallon_to_liters_100km(23.5))

