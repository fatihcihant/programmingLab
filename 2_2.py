# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 00:05:07 2020

@author: fatih cihan
"""

def ınsertionSort(array=[6,5,4,3,2,1]):
    n = len(array)
    for i in range(1,n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array


def shellSort(array=[6,5,4,3,2,1]):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp
        gap //= 2  
    return array

print(shellSort())
print(ınsertionSort())