'''
Ejercicio 68 
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del 
mismo. Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la 
cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
'''

paises = []
habitantes = []

for i in range(5):
    paises.append(input("Ingrese un pais: "))
    habitantes.append(int(input("Ingrese la cantidad de habitantes: ")))
    
for i in range(4):
    for j in range(4-i):
        if paises[j] > paises[j+1]:
            aux = paises[j]
            paises[j] = paises[j+1]
            paises[j+1] = aux
            
            aux = habitantes[j]
            habitantes[j] = habitantes[j+1]
            habitantes[j+1] = aux

print("Paises ordenados alfabeticamente: ", paises)

for i in range(4):
    for j in range(4-i):
        if habitantes[j] < habitantes[j+1]:
            aux = habitantes[j]
            habitantes[j] = habitantes[j+1]
            habitantes[j+1] = aux
            
            aux = paises[j]
            paises[j] = paises[j+1]
            paises[j+1] = aux
            
print("Paises ordenados por cantidad de habitantes: ", paises)

