# Escribe un código que almacene en una variable el *string* "Contraseña". Luego, 
# el programa debe solicitar al usuario "Introducir contraseña", hasta que la palabra ingresada sea correcta.
import os
Contra = input("Ingrese su contraseña: ")
os.system("cls")
print("Contraseña agregada con exito")
while True:
    rev = input("Ingrese la contraseña para acceder: ")
    if rev == Contra:
        print("Contraseña correcta")
        break
    else:
        print("Error, contraseña incorrecta, intente nuevamente")