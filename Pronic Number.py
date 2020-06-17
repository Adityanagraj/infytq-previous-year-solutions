"""
Given a integer we should divide the total number into substrings and we should verify
each num is pronic num or not if pronic we should print that nums in the sorted order

>> Input 1
   272
>> Output 1
   2 72 272
>> Input 2
   12665042
>> Output 2
   2 6 12 42 650
"""
def pronic(n):
    for i in range(1,(n//2)+1):
        if i*(i+1)==n:
            return True
    return False
n=input()
ara=[]
for i in range(len(n)):
    for j in range(i,len(n)):
        x=n[i:j+1]
        ara.append(x)
s=set()
for i in ara:
    if pronic(int(i)):
        s.add(int(i))
x=(sorted(s))
values = ','.join(map(str, x))
values=values.replace(',',' ')
print(values)
