'''
Ejercicio 33 
En el bloque principal del programa definir un diccionario que almacene los nombres de paises como 
clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada clave y 
valor.
'''

def mostrarDiccionario(diccio):
    for i in diccio:
        print(f'La clave es: {i} y el valor es: {diccio[i]}')
        
diccio = {'Argentina':4000000, 'Alemania':5000000, 'Rusia':50000000}
mostrarDiccionario(diccio)

        
    