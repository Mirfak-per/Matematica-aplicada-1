# 1. Escribe una función que reciba dos números y retorne el producto de los números recibidos.
# 2. Escribe una nueva función que tome el producto calculado en el ítem anterior
# y redondee el valor al entero.
# 3. Pide al usuario que ingrese dos números, y utiliza ambas funciones para imprimir el valor
# de la multiplicación redondeado al entero.
def Producto2num():
    while True:
        try:
            x = float(input("Ingrese un numero entero: "))
            i = float(input("Ingrese el segundo numero: "))
            break
        except:
            print("Error,Ingrese nuevamente, no se aceptan numeros escritos ej: NO se aceptan: 'dos' ")
    producto = x * i
    return producto

def redondeoprod(producto):
    #round redondea al valor mas cercano 
    return round(producto)


Producto = Producto2num()

redondeo = redondeoprod(Producto)

print(f"El los numeros que ingreso al ser multiplicados y luego redondeados son {redondeo}")