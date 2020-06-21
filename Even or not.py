"""
A string which is a mixture of letter and integer and special char from which 
find the largest even number from the available digit after removing the duplicates.

>>Input 1
  infosys@337
>>Output 1
  -1
>>Input 2
  Hello#81@21349237
>>Output 2
  9874312
"""
import itertools
n=input()
ss=set()
m=-1
for i in n:
    if i.isdigit():
        ss.add(i)
x=list(itertools.permutations(ss,len(ss)))
for d in x:
    k=''.join(d)
    if int(k)%2==0 and int(k)>m:
        m=int(k)
print(m)