# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:55:36 2020

@author: fatih cihan
"""

def myPow(a,b):
    if b ==0:
        return 1
    elif b == 1:
        return a
    else:
        if b%2==0 :
            return myPow(a*a,b//2)
        else:
            return myPow(a*a,b//2)*a

print(myPow(2,5))
print(myPow(2,4))



myList = [4,-3,5,-2,-1,2,6,-2]
maxi = 0
for i in range(len(myList)):
    for j in range(i,len(myList)):
        t = 0
        for k in range(i,j):
            t = t + myList[k]
        if maxi<t:
            maxi = t
            f_ind = i
            l_ind = j-1
print(maxi,f_ind,l_ind)


def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        if b%2 == 0:
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)*a

print(power(3,7))



mylist = [4,-3,5,-2,-1,2,6,-2]
maxi=0
for i in range(8):
    for j in range(i,8):
        t=0
        for k in range(i,j):
            t=t + myList[k]
        if maxi<t:
            maxi=t
            i_1 , i_2 = i,j
print(maxi,i_1,i_2)


