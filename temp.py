from os import *
from sys import *
from collections import *
from math import *

def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def sort_list(lst, i):
    x = lst[i:]
    x = sorted(x)
    lst[i:] = x

def nextPermutation(permutation, n):
    min = -1
    min_pos = n-1
    for i in range(n-2, -1, -1):
        if permutation[i] < permutation[i+1]:
            swap(permutation, i, min_pos)
            sort_list(permutation, i+1)
            return permutation
        if (permutation[i] > permutation[n-1]) and (min == -1 or permutation[i] < min):
            min = permutation[i]
            min_pos = i
    permutation.reverse()

    return permutation

print(nextPermutation([1,3,2], 3))