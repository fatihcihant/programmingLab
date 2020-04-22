# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:44:20 2020

@author: fatih cihan
"""

from sympy import Symbol,Limit

t = Symbol('t')
t1 = Symbol('t1')
delta_t = Symbol('delta_t')


St = 5*t**2 + 2*t + 8

St1 = St.subs({t:t1})
St1_delta = St.subs({t: t1 + delta_t})

f_limit = Limit((St1_delta - St1)/delta_t,delta_t,0).doit()
print("{} fonk limiti: {}".format(St,f_limit))