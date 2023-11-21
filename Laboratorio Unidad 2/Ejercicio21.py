"""
Ejercicio 21 
Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad constante (m/s) durante un tiempo t (s), 
considerar que es un MRU (Movimiento Rectilíneo Uniforme).  
Se sabe que el cálculo de la velocidad en MRU es por formula:  𝑽 = 𝑫/𝑻 
Despejando la distancia se tiene: 𝑫=𝑽 𝒙 𝑻 
"""

v = int(input("Ingrese la velocidad del movil en m/s: "))
t = int(input("Ingrese el tiempo en segundos: "))
d = v * t
print("La distancia recorrida es: ",d,"m.")

