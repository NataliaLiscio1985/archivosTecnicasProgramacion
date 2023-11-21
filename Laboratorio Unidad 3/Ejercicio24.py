"""
Ejercicio 24 
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: 
cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó 
correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el 
nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que: 
 
• Nivel máximo: Porcentaje>=90%. 
• Nivel medio: Porcentaje>=75% y <90%. 
• Nivel regular: Porcentaje>=50% y <75%. 
• Fuera de nivel: Porcentaje<50%. 
"""

preguntas = int(input("Ingrese la cantidad de preguntas: "))
correctas = int(input("Ingrese la cantidad de preguntas correctas: "))
porcentaje = (correctas * 100) / preguntas
if correctas >= 90:
    print("Nivel máximo")
elif correctas >= 75 and correctas < 90:
    print("Nivel medio")
elif correctas >= 50 and correctas < 75:
    print("Nivel regular")
else:
    print("Fuera de nivel") 
    