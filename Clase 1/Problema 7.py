# La fórmula que permite convertir los grados Celsius a Fahrenheit es la siguiente:
# F = (9/5)C + 32
# 1. Crea una función que permita realizar esta conversión.
# 2. Luego, pide al usuario que ingrese la temperatura en grados Celsius y utiliza la función para calcular su equivalente en grados Fahrenheit.
# 3. Imprime el resultado redondeado a la centésima.

def ctof():
    while True:
        try:
            x = float(input("Ingrese grados celcius para transformar a fahrenheit: "))
            break
        except:
            print("Error, Ingrese un numero valido, como '2,-2, 0.2 , -0,2 '")
    ctof1 = ((9/5)*x) +32
    round(ctof1,2)
    return ctof1

ctof2 = ctof()
print(f"Los grados celcius transformados a gahrenheit y redondeados a la cestesima (dos decimales) es: {ctof2}")