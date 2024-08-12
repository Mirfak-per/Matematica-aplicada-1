# El Índice de Masa Corporal (IMC) es una medida que se utiliza para evaluar si una persona se encuentra en un peso saludable con respecto a su estatura.
# La fórmula para calcular esta medida es:
# {IMC}= peso(kg) / altura(m)^2

# * Bajo peso: IMC menor a 18,5 
# * Peso normal: IMC entre 18,5 y 24,9 
# * Sobrepeso: IMC entre 25  y 29,9 
# * Obesidad: IMC de 30 o mayor

# 1.Considerando la información entregada, implementa un código que permita calcular mediante una función, el valor del IMC de una persona.
# Luego, solicita al usuario valores de masa y altura e indica, mediante el uso de condicionales, la categoría de la persona según el IMC calculado.

# 2.Considera la siguiente tabla de valores, que muestra el peso y el IMC de once estudiantes. Guarda los valores del IMC en una lista e imprime en pantalla los estudiantes que,
# según el criterio de la OMS, están en bajo peso. Además, para cada IMC que esté en bajo peso, índica también el índice en la lista donde se encuentra.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
pesos = [29.5, 37.3, 38, 31, 36, 40.4, 47, 43, 36, 40.1, 27]
imc = [16.43, 19.31, 10.25, 18.63, 17.85, 19.76, 23.64, 21.94, 21.3, 22.67, 16.48]

def unimc():
    while True:
        try:
            Peso= float(input("Ingrese su peso en kg: "))
            altura = float(input("Ingrese su altura en metros: "))
            break
        except:
            print("Error, Ingreso un numero no valido, intente otra vez")
    imc= Peso/(altura**2)
    print(imc)

def valoresimc(numeros,pesos,imc):
    for i in range (len(numeros)):
        if imc[i] < 18.5:
            print(f"El alumno {numeros[i]}, de peso {pesos[i]}, imc {imc[i]}, esta bajo el peso segun el criterio de la oms")


print("1. Calcular imc personal")
print("2. Ver imc bajo peso en la lista de alumnos")
opc = input("Ingrese un numero 1-2")
if opc == "1":
    unimc()
elif opc == "2":
    valoresimc(numeros,pesos,imc)
elif opc == "3":
    print("Saliendo...")
else:
    print("Ingrese una opcion valida")