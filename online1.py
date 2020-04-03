# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:07:23 2020

@author: fatih cihan


#listedeki elemanlari listeelemani ve sayisi seklinde myD dictionaryde olusturulacak
def myH(list1):
    myD= dict()
    for i in list1:
        if i in myD:
            myD[i] = myD[i] +1
        else:
            myD[i]=1
    return myD
list1=[0,5,25,100,5,5,0,100]
print(myH(list1))


def lookUp(dic,val):#dict value
    for k in dic:
        if dic[k]==val:
            return k
        else:    
            return -1

print(lookUp(myD,3))


known={0:0,1:1}
def fiboRec(n):
    

    if n<2:
        return n
    else:
        return fiboRec(n-1) + fiboRec(n-2)
    

    if n in known:
        return known[n]
    else:
        result = fiboRec(n-1) + fiboRec(n-2)
        known[n]=result
        return result
print(fiboRec(7))



    































