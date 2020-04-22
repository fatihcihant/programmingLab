# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:47:48 2020

@author: fatih cihan
"""

from sympy import exp,sqrt,pi,Integral
from sympy import Symbol,pprint

x = Symbol('x')

p = exp(-(x - 10)**2/2)/sqrt(2*pi)
func_integral = Integral(p,(x,11,12)).doit().evalf()

print(func_integral)