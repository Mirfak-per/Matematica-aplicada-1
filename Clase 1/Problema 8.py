# 1. Escribe un código que importe el módulo random y utiliza la función randint() para generar diez números aleatorios entre 1 y 100, y almacénalos en una lista.
# 2. Imprime en pantalla la lista con los diez números generados.
# 3. Utiliza la indexación en Python para acceder al segundo y sexto elemento de la lista.
#    Ten en cuenta que en Python los índices comienzan en 0. ¿Cómo imprimirías estos elementos?
import random
lista = []
for i in range (10):
    lista.append(random.randint(1,100))

print(lista)

print(f"El segundo y sexto elemeno de la lista es {lista[1]} y {lista[5]} ")