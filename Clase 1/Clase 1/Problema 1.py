# Escribe un código que pida al usuario ingresar un número real 
# y determine si el número ingresado es positivo, negativo o cero.
while True:
    try:
        x = int(input("Ingrese un numero entero: "))
        break
    except:
        print("Error,Ingrese nuevamente, no se aceptan numeros decimales o numeros escritos")

if x > 0:
    print(f"El numero {x} es positivo")
elif x < 0:
    print(f"El numero {x} es negativo")
else:
    print("El numero es 0 / neutro")