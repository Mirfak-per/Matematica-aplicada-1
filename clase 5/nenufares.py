nenufar = 3

for i in range(20):
    if i == 0:
        print("dia: ",i+1,"cantidad de nenufares",nenufar)
    else:  
        print("dia: ",i+1,"cantidad de nenufares",nenufar*2)
        nenufar = nenufar *2
    
print((4.5/3),(6.75/4.5),(10.125/6.75))

"""
r = An+1/An = An/an-1

An = a1 * r**(n-1)


2 = a1 * 0.2 **6

2/0.2**6= a1

31250 = a1
###########

An = 31250 * 0.2 ** (n-1)

"""

for i in range(20):
    if i == 0:
        print("dia 1=",31250 * 0.2 ** (i+1-1))
    else:
        print(f"dia:",{i+1},"el termino es",{round(31250 * 0.2 ** (i+1-1))})