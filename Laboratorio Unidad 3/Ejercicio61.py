'''
Ejercicio 61 
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de 
persona menor en orden alfabético.
'''

lista = []
for i in range(5):
    lista.append(input("Ingrese un nombre: "))
    
lista.sort()
print("El menor nombre de la lista es: ", lista[0])
