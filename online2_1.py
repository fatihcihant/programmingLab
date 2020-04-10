# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:39:11 2020

@author: fatih cihan
"""

from sympy import Symbol
from sympy import factor,expand
from sympy import pprint

x = Symbol('x')
y = Symbol('y')

#

y = 1
y = y + 1
print(y)

x = Symbol('x')
x = x + 1
print(x)

#
x=Symbol('x')
y=Symbol('y')

p=x *(x + x) 
print(p)

#

x = Symbol('x')
y = Symbol('y')

p = (x + 2)*(x + 3)
print(p) #--> (x + 2)*(x + 3)

#

expr = x**2 - y**2
factors = factor(expr)#icine girilen ifadeyi carpanlarina ayirir

expands = expand(factors)#carpanlarina ayrilan ifadenin acilimini yazar

print(expands)
print(factors,"->",expands) #detayli yazilmis hali

#

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
print(expr)
factors = factor(expr)
print(factors) 

                
pprint(factors) 

#

series = x
n=5
for i in range(2,n+1):
    series = series + (x**i)/i

print(series) #5.dereceden bilinmeyen denklemi yazdirir

pprint(series) 
               
#

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2})
print(res) #9
res2 = expr.subs({x:1-y}) #x'i yok et.
print(res2) #x olmayan denklem

#

series = x
n = 5
x_value = 5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)
series_value = series.subs({x:x_value})
print(series_value) # 10085/12