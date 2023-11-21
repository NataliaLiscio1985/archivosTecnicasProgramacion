'''
Ejercicio 49 
Escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una 
lista en la que todos los números aparezcan no más de una vez. 
Nota: Asume que la lista original está ya dentro del código - no tienes que ingresarla desde el teclado.  
Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal - no necesitas 
actualizar la lista actual. 
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

my_list = new_list
print(my_list)



