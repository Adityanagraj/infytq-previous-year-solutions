"""
Task is to print all the possibilities of the string till the length of the given string.

>>Input
  abc
>>Output
  a
  b
  c
  ab
  ac
  ba
  bc
  ca
  cb
  abc
  acb
  bac
  bca
  cab
  cba
"""


import itertools 
x=input()
perms=list(itertools.permutations(x,1))
perms1=list(itertools.permutations(x,2))
perms2=list(itertools.permutations(x,3))
for i in perms:
    print(''.join(i))
for j in perms1:
    print(''.join(j))
for k in perms2:
    print(''.join(k))