'''
Ejercicio 6 
Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo. 
Por ejemplo, 8 no es un número primo, ya que puedes dividirlo entre 2 y 4 (no podemos usar divisores 
iguales a 1 y 8, ya que la definición lo prohíbe). 
Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el. 
Tu tarea es escribir una función que verifique si un número es primo o no. 
 
La función: 
• se llama is_prime; 
• toma un argumento (el valor a verificar) 
• devuelve True si el argumento es un número primo, y False de lo contrario. 
 
Sugerencia: intenta dividir el argumento por todos los valores posteriores (comenzando desde 2) y 
verifica el resto - si es cero, tu número no puede ser un número primo; analiza cuidadosamente cuándo 
deberías detener el proceso utilizando la raíz cuadrada de cualquier valor pasado, puedes utilizar el 
operador **.  
Recuerda: la raíz cuadrada de x es lo mismo que x 0.5 (num ** 0.5) 
 
Complementa el código en el editor. 
Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
'''
def is_prime(numero):
    acum=0
    if numero > 1:
        for i in range (2, numero):
            if numero % i == 0:
                acum += 1
    if acum == 0:
        return True


if is_prime(int(input("Ingrese un numero: "))):
    print("El numero es primo")
else:
    print("El numero no es primo")
    
