from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
from colorama import  init, Fore, Style
init(autoreset=True)

"""
diferencia entre  un termino y el anterior = 4 (termino 2 - termino 1)

a10 = -20 el resultado de el termino 10

n = 10 el numero del que se saca el resultado anterior

formula:
An = A1 + (n-1) * d

"""
def A(n):
    return  -56 + (n-1) * 4
print(Fore.RED+ str(A(100))+ " es el resultado de el termino 100")


cont = 400
while cont < 440:
    cont += +1
    print(Fore.GREEN+"n= "+str(cont)+" An ="+str(A(cont)))