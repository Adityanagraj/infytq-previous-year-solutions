"""
Print all the possibilities of the given string of length of the string

>>Input 1
  ab
>>Output 1
  ab
  ba
>>Input 2
  abc
>>Output 2
  abc
  acb
  bac
  bca
  cab
  cba
"""
from itertools import permutations
x=input()
perms = [''.join(p) for p in permutations(x)]
for i in perms:
    print(i)