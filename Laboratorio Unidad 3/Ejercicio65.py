'''
Ejercicio 65 
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una. 
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. 
Mostrar esta tercer lista.
'''

lista1 = []
lista2 = []
lista3 = []

print('Carga Primer lista')
for i in range (4):
    lista1.append(int(input("Ingrese un numero en la posicion: ")))
    
print('Carga Segunda lista')
for i in range (4):
    lista2.append(int(input("Ingrese un numero : ")))

for i in range (4):
    lista3.append(lista1[i] + lista2[i])   
    
print('Lista 3')
print(lista3)

