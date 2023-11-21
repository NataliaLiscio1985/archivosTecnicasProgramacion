"""
Ejercicio 6 
Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada 
secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número 
secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán 
atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el 
código. 
 
Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código: 
 
 Información Privada 
• pedirá al usuario que ingrese un número entero; 
• utilizará un bucle while; 
• comprobará si el número ingresado por el usuario es el mismo que el número escogido por el 
mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario 
debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un 
número nuevamente. Si el número ingresado por el usuario coincide con el número escogido 
por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes 
palabras: "¡Bien hecho! Eres libre ahora." 
 
INFO EXTRA   
Por cierto, observa la función print(). La forma en que lo hemos utilizado aquí se llama impresión 
multilínea. Puedes utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la 
lectura del texto o crear un diseño especial basado en texto. Experimenta con ello.
"""

secret_number = 777
print(
    """
    +================================+
    | Bienvenido a mi juego          |
    | Introduce un numero entero     |
    | y adivina que numero he        |
    | elegido para ti.               |
    | ¿Cual es el numero secreto?    |
    +================================+    
    """
)
numero_elegido = int(input("Introduce un numero entero: "))
while numero_elegido != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero_elegido = int(input("Introduce un numero entero: ")) 

print("El numero es: ",secret_number,"\n¡Bien hecho! Eres libre ahora.")
