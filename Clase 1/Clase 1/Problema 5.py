# Escribe un código que, utilizando un ciclo for, pida al usuario ingresar un número entero 
# y muestre la tabla de multiplicar desde el 1 al 12 de dicho número.

while True:
    try:
        x = int(input("Ingrese un numero entero: "))
        break
    except:
        print("Error,Ingrese nuevamente, no se aceptan numeros decimales o numeros escritos")

ix = 1

for i in range(12):
    print (f"{x} x {ix} = {x*ix}")
    ix += +1