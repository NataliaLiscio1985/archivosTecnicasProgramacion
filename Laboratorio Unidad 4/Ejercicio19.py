'''
Ejercicio 19 
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los 
valores hacerlo por teclado.
'''
def ingresoEntero():
    entero = int(input("Ingrese un entero: "))
    return entero

def cargaTresEnteros():
    lista=[]
    for i in range(3):
        lista.append(ingresoEntero())
    return lista

def mayorDeTres():
    lista = cargaTresEnteros()
    mayor = lista[0]
    for i in range(1,3):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

print(mayorDeTres())

    
    
    




