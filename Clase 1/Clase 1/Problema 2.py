# Escribe un código que pida al usuario ingresar un número entero 
# y que determine si el número ingresado es par o impar.

while True:
    try:
        x = int(input("Ingrese un numero entero: "))
        break
    except:
        print("Error,Ingrese nuevamente, no se aceptan numeros decimales o numeros escritos")

if x % 2 == 0:
    print(f"El numero {x} es par")
elif x % 2 != 0:
    print(f"El numero {x} es impar")