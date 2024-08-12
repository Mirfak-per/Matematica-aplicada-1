# Escribe un código que, mediante un ciclo while, sume los primeros 100 números naturales.
x= 0
I = 1
while True:
    print(F"{x} + {I} = {x+I}")
    x = x+I
    I += +1
    if I == 101: 
        break