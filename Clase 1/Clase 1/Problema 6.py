# 1. Escribe una función que reciba dos números y retorne el producto de los números recibidos.
# 2. Escribe una nueva función que tome el producto calculado en el ítem anterior
# y redondee el valor al entero.
# 3. Pide al usuario que ingrese dos números, y utiliza ambas funciones para imprimir el valor
# de la multiplicación redondeado al entero.
def Producto2num():
    while True:
        try:
            x = int(input("Ingrese un numero entero: "))
            i = int(input("Ingrese el segundo numero: "))
            break
        except:
            print("Error,Ingrese nuevamente, no se aceptan numeros decimales o numeros escritos")
    producto = x * i
    return producto

def 
Producto = Producto2num()

