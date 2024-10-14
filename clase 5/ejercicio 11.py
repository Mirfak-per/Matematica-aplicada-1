
"""
d = ?
a3 = 500
a10  = 1501
n = 3, 10


an = a1 +(n-1) * d

500 = A1 + (3-1) * d

500 = a1 + 2d

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

an = a1 +(n-1) * d

1501 = a1 + (10 -1) * d

1501 = a1 + 9d

###########################

    500 = a1 + 2d
    1501 = a1 + 9d
-
~~~~~~~~~~~~~~~~~~~~~~~
1001 = 7d
1001/7 = d
143 = d

###############

500 = A1 + (3-1) * 143

500 = a1 + 4 * 143
500 = a1 + 286
500 - 286 = a1
214  =a1
#############################

a1 = 214
d= 143

An = 214 +(n-1)*143
"""
from colorama import init, Fore, Style

    # TODO: Define form fields here

def A(n):
    return 214 + (n-1) *143

print(Fore.BLUE+str(A(1)))

print(Fore.RED+str(A(31)))

print( Fore.YELLOW+"5505    "+str(round((5505-214)/143) +1) +" = n "+ str(A(38)))
print(38/31)