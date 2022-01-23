'''
Numerical Integration 
Simpson's rule

language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

from math import exp
from scipy import integrate 

def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result
    
g = lambda y: exp(-y**2)
a = 0
b = 2

print ('n         midpoint')
for i in range(1, 21):
    n = 2**i
    m = midpoint(g, a, b, n)
    print (n, m)
    
# 2-point Gauss integration    
f = lambda x: x**8 + x**4 
intf = integrate.quadrature(f, 0.0, 1.8) 
print(intf)
